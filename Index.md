---
layout: default
title: 汉化发布
permalink: /
---
<div class="xz-infotable-block">
  <table class="table infoTable">
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
          <tr><td class="infoTableImage" colspan="2"><img src="https://file.moetu.org/images/2020/05/16/ce2bf2658068ebd84eae751b5afce47e526a8a0b6793ced7.jpg" alt="日本发行版游戏封面|none"></td></tr>
          <tr><th>开发商</th><td>GREZZO</td></tr>
          <tr><th>发行商</th><td>任天堂</td></tr>
          <tr><th>平台</th><td>任天堂 3DS</td></tr>
          <tr><th>发售日期</th><td>2018 年 11 月 8 日</td></tr>
          <tr><th>分级</th><td>CERO：A</td></tr>
          <tr><th class="infoTableFoot" colspan="2"><a href="https://www.nintendo.co.jp/3ds/bgnj/pc/index.html">官方网站</a></th></tr>
      </tbody>
  </table>
</div>

## 发布链接
- Github：[https://github.com/Xzonn/LuigiMansion/releases/latest/](https://github.com/Xzonn/LuigiMansion/releases/latest/)。
- 百度网盘：[https://pan.baidu.com/s/1wlbfWbSADaq5loOgv248Og](https://pan.baidu.com/s/1wlbfWbSADaq5loOgv248Og)（08mw）。
{: .text-left }

## 1.0版汉化说明
这游戏发售到目前（2020/05/15）已经一年半了，汉化版版本号竟然还没到1.0。本来我以为这个游戏会有别的汉化组汉化，结果我自己鼓捣这么久都没看到别的汉化组开坑，所以我就把我自己拙劣的汉化成果发布了出来。如果哪位愿意帮我润色或者干脆从头开始翻译的话，可以和我联系。当然，用我的工具自己翻译也是可以的。

本次更新的版本号是1.0，说明这个版本是正式发布版本。正式版和之前的版本有以下的区别：

- 采用了完全重构的文本导入导出工具，并用新工具调整了部分对话的长度和语序。
- 修正了几处不合理的翻译。
- 改定了两处译名：哎呦·喂 → 哎哟·喂（官译如此，之前是我打错了）；嘘嘘鬼 → 害羞幽灵（新官译，即繁中译名简体化）。
- 根据上述译名更改，同时修改了害羞幽灵的名字：嘘嘘某 → 害羞某，此外根据《路易吉洋馆2／3》的官译修改了<span lang="ja">テレワン</span>到<span lang="ja">テレジュ</span>的译名：谐音 → 原意（嘘嘘艺 → 害羞一号）。
- 去除了哎哟·喂博士登场时附加的说明文本。
- 微调了字库的样式。

此外，文本导入导出工具以GPL-3.0协议开源并发布在GitHub上，采用Python 3.0编写，导出格式为markdown（因为方便预览）。您可以修改并用于其他用途，只要遵守GPL-3.0协议（开源）即可。链接：<https://github.com/Xzonn/LuigiMansion/blob/master/Text.py>。本人仅测试了《路易吉洋馆》日文版的文本文件（main.gmsg），不保证在其他语言版本或其他游戏的文本文件中可用。

请确认您的Luma版本为最新版（<https://github.com/LumaTeam/Luma3DS/releases/latest>），且已在设置中开启“Enable game patching”（允许游戏补丁）选项。

将本补丁的“luma”文件夹解压到SD卡的根目录即可使用。如提示合并或覆盖，均选择确认。

另外，我个人不是很喜欢“路易吉鬼屋”这个译名，因为原名里面没有“鬼”这个要素。而且，这个游戏也不是恐怖游戏。

关于版权和使用的说明请参考下文。

## 原汉化说明
我本人从《Nintendo Direct 2018.3.9》初次公布的时候就开始关注这个游戏了，因为之前通关过《路易吉洋馆２》，感觉挺有意思。但是因为港任大概已经放弃了 3DS，因此当时就觉得这作有官方中文的可能性不大。果然，直到日本版发售后都没有官方中文的消息，因此我开始尝试自己汉化。

因为一些巧合，我发现这个游戏的文本和字库都有前辈研究过，但研究得并不完善。在经过一段时间的尝试后，我终于可以基本稳定地导出、导入文本，并修改字库了。因此，这个游戏汉化的技术问题基本已经解决，剩下的任务就是翻译了。

然而，由于我研究的是日文文本，我本人的日语水平有限，而日翻本来也比英翻数量少，因此我只能自学日语，并依靠谷歌翻译和英文文本对照，勉强把所有文本都翻译完了。因为个人能力有限，可能会有些翻译错误的地方，还请不吝赐教。

感谢任天堂和 GREZZO 开发了这么有趣的游戏，感谢神游 iQue 对《路易吉洋馆２》中文本地化作出的贡献。“哎哟·喂”、“鬼怪吸尘器”等译名均使用了神游制定的官方译名。

感谢 [IcySon55](https://github.com/IcySon55) 等人开发的 [Kuriimu](https://github.com/IcySon55/Kuriimu) 项目对本人研究文本、字库提供了思路。如果您对本作的文件格式有兴趣，可以参考 **[这篇文章](https://xzonn.github.io/Luigi-Mansion-Chinese-Localization/)**。

由于版权问题，本人汉化发布仅提供 Luma 重定向补丁。如需使用，请将压缩文件内的全部文件 **直接** 解压到 SD 卡的根目录下。

反馈链接：

- **[直接在本页下方留言](#xz-comment)**
- **[通过 GitHub 的“issues”功能](https://github.com/Xzonn/LuigiMansion/issues)**
- **[通过 Bilibili 的“私信”功能](https://message.bilibili.com/#whisper/mid16114399)**

本汉化允许转载，但请至少保留汉化者的名字（Xzonn），这是对我最基本的尊重，谢谢配合。**不欢迎不规范转载。**

**声明：本人对游戏软件仅做研究用途，本人不提供软件本体，也从未对软件本体进行非法传播，更未对其用作商业用途。如因非法传播造成法律纠纷，概与本人无关。特此声明。**

**为方便汉化版本更新以及汉化版本出现问题后的处理，请直接使用 Luma 重定向补丁。任何将本补丁重新打包再发布的行为造成的后果概与本人无关。**

## 更新日志
- 1.0.2（2022/07/29）：
  - 修正了一处错误翻译。
- 1.0.1（2022/04/19）：
  - 修正了一处错误翻译。
- 1.0.0（2020/05/15）：
  - 采用了完全重构的文本导入导出工具，并用新工具调整了部分对话的长度和语序。
  - 修正了几处不合理的翻译。
  - 改定了两处译名：哎呦·喂 → 哎哟·喂（官译如此，之前是我打错了）；嘘嘘鬼 → 害羞幽灵（新官译，即繁中译名简体化）。
  - 根据上述译名更改，同时修改了害羞幽灵的名字：嘘嘘某 → 害羞某，此外根据《路易吉洋馆2／3》的官译修改了<span lang="ja">テレワン</span>到<span lang="ja">テレジュ</span>的译名：谐音 → 原意（嘘嘘艺 → 害羞一号）。
  - 去除了哎哟·喂博士登场时附加的说明文本。
- 0.9.6（2019/06/21）：
  - 根据任天堂香港公布的视频，修改“グーイージ”译名为“傀易吉”。
  - 修正“ウォーターモプー”译名为“水莫普”。
- 0.9.5（2019/04/09）：
  - 更新与地点名称相关的字库。
  - “<span lang="ja">ポール・ロング</span>”的译名由“宝灵”修改为“泰丘”（此鬼怪设定为台球运动员）。
  - 将“某按钮”修改为“某键”（例：<kbd>A</kbd>键）。
  - 小幅修改部分文本。
- 0.9.4（2019/04/06）：
  - 重新检查了成就的描述，修改部分用语。
  - 删除指向性言论。
- 0.9.3（2019/04/05）：
  - 小幅修改部分文本。
  - 对比《路易吉洋馆２》的官方翻译文本，将“路易吉君”全部替换为“路易吉”。
- 0.9.2（2019/03/28）：
  - 小幅修改部分文本。
- 0.9.1（2019/03/25）：
  - 修正了获得害羞幽灵雷达后的死机问题。
  - 修改了部分字符的字体。
- 0.9.0（2019/03/24）：
  - 此为最初版本。

## 常见问题
- Q：我不想读下面这么多字，怎么办？
  - A：最重要的三句：我不会发布 .3ds/.cia 格式的文件，更新了百度网盘链接，转载请至少保留发布者的名字。
- Q：能否发布 .3ds/.cia 格式？
  - A：很明确地告诉您，现在不会发布，以后也不会。原因请见发布说明的最后一句话。如有需求请自行制作，或求助于他人。
- Q：我在安装 .cia 文件时出现了错误，应该怎么办？
  - A：我不知道。我本人没有发布过 .cia 格式，请自行询问发布者。
- Q：Luma 重定向补丁适用于什么版本的游戏？
  - A：抱歉，我忘记在最初的发布说明中提到了。此补丁用于日本发行版游戏，Title ID 为 00040000001D1800。
- Q：我该如何获取游戏本体？
  - A：实体版可以[在日本亚马逊上购买](https://www.amazon.co.jp/gp/product/B07HC5JW8H)，下载版可以[在任天堂官网购买](https://www.nintendo.co.jp/titles/50010000046735)。
- Q：我在 Github 上下载速度较慢，请问可否提供其它链接？
  - A：抱歉，我最初发布时没有考虑到这点。我已经补充了[百度网盘的链接](https://pan.baidu.com/s/1wlbfWbSADaq5loOgv248Og)，提取码为`08mw`。
- Q：我在安装 Luma 重定向补丁后打开游戏报错，请问是怎么回事？
  - A：根据目前我掌握的消息，这可能是由于您的 Luma 版本是不稳定的开发版。经测试，原作者发布的 [v9.1](https://github.com/AuroraWright/Luma3DS/releases/tag/v9.1) 版可以正常运行，[luma-hourlies](https://github.com/hax0kartik/luma-hourlies) 项目编译的 [90-luma3ds-bd15f51](https://github.com/hax0kartik/luma-hourlies/releases/tag/90-luma3ds-bd15f51) 版也可以正常运行。如果您对 Luma 不是很了解，请尝试替换为上述两个版本之一。（替换方式：下载文件，将`boot.firm`拷贝到 SD 卡根目录下，覆盖原有文件即可）
- Q：我安装了 Luma 重定向补丁，但打开游戏仍为日文，请问是怎么回事？
  - A：请在 3DS 主机开机时按住<kbd>SELECT</kbd>键，如果直接进入 3DS 界面，说明您没有安装 Luma，请自行查找教程安装。如果出现设置界面，请检查 Luma 版本是否高于 7.0（如果您不确定 Luma 版本，请替换为上一条链接中的两个版本之一）。如果版本无误，请勾选“`Enable game patching`”。设置完毕后按<kbd>START</kbd>保存。
- Q：是否可以转载此汉化？
  - A：欢迎转载，但建议您保留发布者信息、发布说明和更新地址，以便我及时得到反馈。如果条件不允许，请至少保留汉化者的名字（Xzonn），这是对我最基本的尊重，谢谢配合。当然，不保留发布者信息直接转载者，我也没有办法，只能在之后的发布说明中将您的名字写到这里。

## 汉化预览
<div class="row">
  <div class="col-sm-6"><img src="https://file.moetu.org/images/2020/05/16/9e0dadd8dcb3f8e7fc31ea2d4ab69284e4bb926f60c038e9.png" alt="标题界面"/></div>
  <div class="col-sm-6"><img src="https://file.moetu.org/images/2020/05/16/eb35c92e62d24e6792062ecc5ef88e7933cb057e36045563.png" alt="存档选择界面"/></div>
  <div class="col-sm-6"><img src="https://file.moetu.org/images/2020/05/16/2c26eac8a2e45f5f9d18dfb2b1ee0e98e8f271bdb0d3d789.png" alt="实验室界面"/></div>
  <div class="col-sm-6"><img src="https://file.moetu.org/images/2020/05/16/14d1290b462d4fb72a46efa79bc166286464b431c6617dea.png" alt="游戏界面"/></div>
</div>

<div class="bilibiliBox" data-aid="45332875" data-page="1"></div>

## 游戏介绍
《**路易吉洋馆**》是 2018 年 11 月 8 日于日本发行的任天堂 3DS 游戏。该游戏是 GameCube 游戏《路易吉洋馆》的重制版，在原版的基础上加入了闪光灯、Amiibo、双人游玩等元素。其续作《**路易吉洋馆2**》（繁体：《**路易吉洋樓2**》，日文：『<strong lang="ja">ルイージマンション２</strong>』）于 2013 年发售，港台版自带简繁中文支持。

## 操作方式
- 移动：左摇杆
- 调查／开门／呼喊马力欧：<kbd>X</kbd>
- 闪光灯／跳过剧情：<kbd>A</kbd>
- 使用 Game Boy Horror 搜索：<kbd>Y</kbd>
- 切换正常移动和横向移动：<kbd>B</kbd>
- 改变路易吉的朝向：陀螺仪／C 摇杆
- 射出元素／吹气：<kbd>L</kbd>（+<kbd>A</kbd>：射出元素球）
- 使用鬼怪吸尘器：<kbd>R</kbd>
- 暂停／跳过最终战斗前的过场动画：<kbd>START</kbd>
- 触摸屏可以用来查看地图、鬼怪、收集品，或与哎哟·喂博士联系。