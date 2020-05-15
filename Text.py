#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Credit to: Xzonn
# 2020-05-14

import json, re, struct

_knownCommands = {
    0x08: 2,
    0x0E: 2,
    0x0F: 2,
    0x11: 1,
    0x19: 4
}

_alignCommands = [0x08, 0x0E, 0x0F, 0x19]

def BytesToString(byteString):
    unicodeString = [byteString[i] + 256 * byteString[i + 1] for i in range(0, len(byteString), 2)]
    s = ""
    i = 0
    while i < len(unicodeString):
        c = unicodeString[i]
        if c == 0x7f:
            i += 1
            c = unicodeString[i]
            if c == 0:
                i = len(unicodeString)
                continue
            if c == 1:
                s += "<br>"
                i += 1
                continue
            if c == 2:
                s += "<hr>"
                i += 1
                continue
            if c == 0x15:
                if i % 2 == 0:
                    i += 1
                if unicodeString[i + 1] == 0xFFFF:
                    assert unicodeString[i + 2] == 0xFFFF
                    s += "</span>"
                    i += 2
                else:
                    s += "<span class=\"color-"
                    i += 1
                    s += hex(unicodeString[i])[2:].upper().zfill(4)
                    s += "\">"
                if i % 2 == 0:
                    i += 1
                i += 1
                continue
            if c == 0x16:
                s += "<ruby>"
                i += 1
                rt = ""
                while unicodeString[i] != 0:
                    rt += chr(unicodeString[i])
                    i += 1
                i += 1
                while not (unicodeString[i] == 0x7F and unicodeString[i + 1] == 0x17):
                    s += chr(unicodeString[i])
                    i += 1
                s += "<rt>" + rt + "</rt></ruby>"
                i += 2
                continue
            s += "[" + hex(c)[2:].upper().zfill(4)
            if c in _alignCommands:
                if i % 2 == 0:
                    i += 1
                for i in range(i + 1, i + 1 + _knownCommands[c], 2):
                    s += "," + hex(unicodeString[i])[2:].upper().zfill(4)
                i += 1
            elif c in _knownCommands:
                for i in range(i + 1, i + 1 + _knownCommands[c]):
                    s += "," + hex(unicodeString[i])[2:].upper().zfill(4)
            s += "]"
        elif c < 32:
            s += "\\x" + hex(c)[2:].zfill(2)
        elif 0xe000 < c < 0xe07f or c == 0xffff:
            s += "\\u" + hex(c)[2:].zfill(4)
        else:
            s += chr(c)
        i += 1
    return s

def StringToBytes(string):
    unicodeString = []
    i = 0
    while i < len(string):
        c = string[i]
        if c == "[":
            end = string.index("]", i + 2)
            codes = [int(i, 16) for i in string[i + 1 : end].split(",")]
            if codes[0] in _alignCommands:
                unicodeString.append(0x7F)
                unicodeString.append(codes[0])
                if len(unicodeString) % 2 == 1:
                    unicodeString.append(0)
                for j in codes[1 : ]:
                    unicodeString.append(j)
                    unicodeString.append(0)
            else:
                unicodeString.append(0x7F)
                unicodeString += codes
            i = end + 1
        elif c == "<":
            end = string.index(">", i + 2)
            tag = string[i + 1 : end]
            if tag == "br":
                unicodeString.append(0x7F)
                unicodeString.append(0x01)
            elif tag == "hr":
                unicodeString.append(0x7F)
                unicodeString.append(0x02)
            elif tag.startswith("span "):
                colorStart = tag.index("color-") + 6
                tagClass = int(tag[colorStart : colorStart + 4], 16)
                unicodeString.append(0x7F)
                unicodeString.append(0x15)
                if len(unicodeString) % 2 == 1:
                    unicodeString.append(0)
                unicodeString.append(tagClass)
                unicodeString.append(0)
            elif tag == "/span":
                unicodeString.append(0x7F)
                unicodeString.append(0x15)
                if len(unicodeString) % 2 == 1:
                    unicodeString.append(0)
                unicodeString.append(0xFFFF)
                unicodeString.append(0xFFFF)
            elif tag == "ruby":
                unicodeString.append(0x7F)
                unicodeString.append(0x16)
                rtStart = string.index("<rt>", end)
                rtEnd = string.index("</rt>", rtStart + 4)
                rt = string[rtStart + 4 : rtEnd]
                ruby = string[end + 1 : rtStart]
                end = string.index("</ruby>", rtEnd + 5) + 6
                for j in rt:
                    unicodeString.append(ord(j))
                unicodeString.append(0)
                for j in ruby:
                    unicodeString.append(ord(j))
                unicodeString.append(0x7F)
                unicodeString.append(0x17)
            i = end + 1
        else:
            unicodeString.append(ord(c))
            i += 1
    unicodeString.append(0x7F)
    unicodeString.append(0x00)
    byteString = struct.pack("<%dH" % len(unicodeString), *unicodeString)
    return byteString

def exportFile(gmsgPath, markdownPath):
    with open(gmsgPath, "rb") as f:
        data = f.read()
    entryCount, startPos = struct.unpack("<II", data[0x0C : 0x14])

    f = open(markdownPath, "w", encoding="utf-8")
    f.write("<style> .color-0001 { color: #39BE39; }  .color-0002 { color: #FF6942; }  .color-0003 { color: #FF9E18; } </style>\n| 编号 | 文本 |\n| --- | --- |\n")
    for i in range(entryCount):
        ID, unknown, offset, length = struct.unpack("<4I", data[startPos + i * 0x10 : startPos + i * 0x10 + 0x10])
        byteString = data[offset : offset + length]
        string = BytesToString(byteString)
        f.write("| %s | %s |\n" % (hex(ID), string))

    f.close()

def importFile(gmsgPath, markdownPath, outputPath):
    PATTERN = re.compile(r"^\| 0x([0-9a-fA-F]+) \| ([^\|]+) \|$", re.M)
    with open(markdownPath, "r", encoding="utf-8") as f:
        text = { int(i[0], 16): i[1] for i in  PATTERN.findall(f.read()) }
    assert len(text) <= 2182

    with open(gmsgPath, "rb") as f:
        data = list(f.read())
    entryCount, startPos = struct.unpack("<II", bytes(data[0x0C : 0x14]))
    newOffset, = struct.unpack("<I", bytes(data[startPos + 0x08 : startPos + 0x0C]))
    for i in range(entryCount):
        ID, unknown, offset, length = struct.unpack("<4I", bytes(data[startPos + i * 0x10 : startPos + i * 0x10 + 0x10]))
        assert ID in text

        string = text[ID]
        byteString = list(StringToBytes(string))

        newLength = len(byteString)
        data[newOffset : newOffset + newLength] = byteString
        newHeadInfo = struct.pack("<4I", ID, unknown, newOffset, newLength)
        data[startPos + i * 0x10 : startPos + i * 0x10 + 0x10] = newHeadInfo
        newOffset += newLength
        if newOffset % 4 > 0:
            newOffset += 4 - newOffset % 4

    with open(outputPath, "wb") as f:
        f.write(bytes(data))

if __name__ == "__main__":
    #exportFile("Original/main.gmsg", "Original/main.md")
    #exportFile("Translated/main.gmsg", "Translated/main.md")
    importFile("Original/main.gmsg", "Translated/main.md", "Translated/main.gmsg")