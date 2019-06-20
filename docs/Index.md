---
layout: default
title: 汉化发布
permalink: /
---
<table class="infoTable">
    <thead>
        <tr><th class="infoTableTitle" colspan="2">路易吉洋馆</th></tr>
        <tr>
            <th class="infoTableSubTitle" colspan="2">
                <div lang="ja">ルイージマンション</div>
                <div lang="en"><em>Luigi's Mansion</em></div>
            </th>
        </tr>
    </thead>
    <tbody>
        <tr><td class="infoTableImage" colspan="2"><img src="https://images-na.ssl-images-amazon.com/images/I/61A3BFk9bYL.jpg" alt="日本发行版游戏封面"></td></tr>
        <tr><th>开发商</th><td>GREZZO</td></tr>
        <tr><th>发行商</th><td>任天堂</td></tr>
        <tr><th>平台</th><td>任天堂 3DS</td></tr>
        <tr><th>发售日期</th><td>2018 年 11 月 8 日</td></tr>
        <tr><th>分级</th><td>CERO：A</td></tr>
        <tr><th class="infoTableFoot" colspan="2"><a href="https://www.nintendo.co.jp/3ds/bgnj/pc/index.html">官方网站</a></th></tr>
    </tbody>
</table>

## 汉化说明
我本人从《Nintendo Direct 2018.3.9》初次公布的时候就开始关注这个游戏了，因为之前通关过《路易吉洋馆２》，感觉挺有意思。但是因为港任大概已经放弃了 3DS，因此当时就觉得这作有官方中文的可能性不大。果然，直到日本版发售后都没有官方中文的消息，因此我开始尝试自己汉化。

因为一些巧合，我发现这个游戏的文本和字库都有前辈研究过，但研究得并不完善。在经过一段时间的尝试后，我终于可以基本稳定地导出、导入文本，并修改字库了。因此，这个游戏汉化的技术问题基本已经解决，剩下的任务就是翻译了。

然而，由于我研究的是日文文本，我本人的日语水平有限，而日翻本来也比英翻数量少，因此我只能自学日语，并依靠谷歌翻译和英文文本对照，勉强把所有文本都翻译完了。因为个人能力有限，可能会有些翻译错误的地方，还请不吝赐教。

感谢任天堂和 GREZZO 开发了这么有趣的游戏，感谢神游 iQue 对《路易吉洋馆２》中文本地化作出的贡献。“哎呦·喂”、“鬼怪吸尘器”等译名均使用了神游制定的官方译名。

感谢 [IcySon55](https://github.com/IcySon55) 等人开发的 [Kuriimu](https://github.com/IcySon55/Kuriimu) 项目对本人研究文本、字库提供了思路。如果您对本作的文件格式有兴趣，可以参考 **[这篇文章](https://xzonn.github.io/Luigi-Mansion-Chinese-Localization/)**。

由于版权问题，本人汉化发布仅提供 Luma 重定向补丁。如需使用，请将压缩文件内的全部文件 **直接** 解压到 SD 卡的根目录下。同时为方便版本控制，将发布于 Github 上。发布链接：**[最新版本](https://github.com/Xzonn/LuigiMansion/releases/latest/)**。

由于没有完整测试，目前版本为预览版。如有翻译错误或死机错误，请及时反馈。如果 1 个月内没有任何反馈，我将发布正式版。

反馈链接：

* **[直接在本页下方留言](#contentComment)**
* **[通过 Github 的“issues”功能](https://github.com/Xzonn/LuigiMansion/issues)**
* **[通过 Bilibili 的“私信”功能](https://message.bilibili.com/#whisper/mid16114399)**
* **[通过百度贴吧的此贴](https://tieba.baidu.com/p/6078283673)**

本汉化允许转载，但请至少保留汉化者的名字（Xzonn），这是对我最基本的尊重，谢谢配合。**不欢迎不规范转载。**

**声明：本人对游戏软件仅做研究用途，本人不提供软件本体，也从未对软件本体进行非法传播，更未对其用作商业用途。如因非法传播造成法律纠纷，概与本人无关。特此声明。**

**为方便汉化版本更新以及汉化版本出现问题后的处理，请直接使用 Luma 重定向补丁。任何将本补丁重新打包再发布的行为造成的后果概与本人无关。**

## 更新日志
* 0.9.5（2019/04/09）：
  * 更新与地点名称相关的字库。
  * “<span lang="ja">ポール・ロング</span>”的译名由“宝灵”修改为“泰丘”（此鬼怪设定为台球运动员）。
  * 将“某按钮”修改为“某键”（例：<kbd>A</kbd>键）。
  * 小幅修改部分文本。
* 0.9.4（2019/04/06）：
  * 重新检查了成就的描述，修改部分用语。
  * 删除指向性言论。
* 0.9.3（2019/04/05）：
  * 小幅修改部分文本。
  * 对比《路易吉洋馆２》的官方翻译文本，将“路易吉君”全部替换为“路易吉”。
* 0.9.2（2019/03/28）：
  * 小幅修改部分文本。
* 0.9.1（2019/03/25）：
  * 修正了获得嘘嘘鬼雷达后的死机问题。
  * 修改了部分字符的字体。
* 0.9.0（2019/03/24）：
  * 此为最初版本。

## 常见问题
* Q：我不想读下面这么多字，怎么办？
  * A：最重要的三句：我不会发布 .3ds/.cia 格式的文件，更新了百度网盘链接，转载请至少保留发布者的名字。
* Q：能否发布 .3ds/.cia 格式？
  * A：很明确地告诉您，现在不会发布，以后也不会。原因请见发布说明的最后一句话。如有需求请自行制作，或求助于他人。
* Q：我在安装 .cia 文件时出现了错误，应该怎么办？
  * A：我不知道。我本人没有发布过 .cia 格式，请自行询问发布者。
* Q：Luma 重定向补丁适用于什么版本的游戏？
  * A：抱歉，我忘记在最初的发布说明中提到了。此补丁用于日本发行版游戏，Title ID 为 00040000001D1800。
* Q：我该如何获取游戏本体？
  * A：实体版可以[在日本亚马逊上购买](https://www.amazon.co.jp/gp/product/B07HC5JW8H)，下载版可以[在任天堂官网购买](https://www.nintendo.co.jp/titles/50010000046735)。
* Q：我在 Github 上下载速度较慢，请问可否提供其它链接？
  * A：抱歉，我最初发布时没有考虑到这点。我已经补充了[百度网盘的链接](https://pan.baidu.com/s/1wlbfWbSADaq5loOgv248Og)，提取码为`08mw`。
* Q：我在安装 Luma 重定向补丁后打开游戏报错，请问是怎么回事？
  * A：根据目前我掌握的消息，这可能是由于您的 Luma 版本是不稳定的开发版。经测试，原作者发布的 [v9.1](https://github.com/AuroraWright/Luma3DS/releases/tag/v9.1) 版可以正常运行，[luma-hourlies](https://github.com/hax0kartik/luma-hourlies) 项目编译的 [90-luma3ds-bd15f51](https://github.com/hax0kartik/luma-hourlies/releases/tag/90-luma3ds-bd15f51) 版也可以正常运行。如果您对 Luma 不是很了解，请尝试替换为上述两个版本之一。（替换方式：下载文件，将`boot.firm`拷贝到 SD 卡根目录下，覆盖原有文件即可）
* Q：我安装了 Luma 重定向补丁，但打开游戏仍为日文，请问是怎么回事？
  * A：请在 3DS 主机开机时按住<kbd>SELECT</kbd>键，如果直接进入 3DS 界面，说明您没有安装 Luma，请自行查找教程安装。如果出现设置界面，请检查 Luma 版本是否高于 7.0（如果您不确定 Luma 版本，请替换为上一条链接中的两个版本之一）。如果版本无误，请勾选“`Enable game patching`”。设置完毕后按<kbd>START</kbd>保存。
* Q：是否可以转载此汉化？
  * A：欢迎转载，但建议您保留发布者信息、发布说明和更新地址，以便我及时得到反馈。如果条件不允许，请至少保留汉化者的名字（Xzonn），这是对我最基本的尊重，谢谢配合。当然，不保留发布者信息直接转载者，我也没有办法，只能在之后的发布说明中将您的名字写到这里。

## 汉化预览
![标题界面](./images/screenshot-1.png)

![存档选择界面](./images/screenshot-2.png)

![实验室界面](./images/screenshot-3.png)

![游戏界面](./images/screenshot-4.png)

<div class="bilibiliBox" data-aid="45332875" data-page="1"></div>

## 游戏介绍
《**路易吉洋馆**》是 2018 年 11 月 8 日于日本发行的任天堂 3DS 游戏。该游戏是 GameCube 游戏《路易吉洋馆》的重制版，在原版的基础上加入了闪光灯、Amiibo、双人游玩等元素。其续作《**路易吉洋馆2**》（繁体：《**路易吉洋樓2**》，日文：『<strong lang="ja">ルイージマンション２</strong>』）于 2013 年发售，港台版自带简繁中文支持。

## 操作方式
* 移动：左摇杆
* 调查／开门／呼喊马力欧：<kbd>X</kbd>
* 闪光灯／跳过剧情：<kbd>A</kbd>
* 使用 Game Boy Horror 搜索：<kbd>Y</kbd>
* 切换正常移动和横向移动：<kbd>B</kbd>
* 改变路易吉的朝向：陀螺仪／C 摇杆
* 射出元素／吹气：<kbd>L</kbd>（+<kbd>A</kbd>：射出元素球）
* 使用鬼怪吸尘器：<kbd>R</kbd>
* 暂停／跳过最终战斗前的过场动画：<kbd>START</kbd>
* 触摸屏可以用来查看地图、鬼怪、收集品，或与哎呦·喂博士联系。