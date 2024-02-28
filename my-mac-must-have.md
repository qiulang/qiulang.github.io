## Mac 装机必备

每次装机都至少要花一两天时间，而且把之前写的装机必备做些更新，这是2023-5-03的版本。我分成两大类，日常使用和开发使用

### 基础软件

1. 输入法： [搜狗](https://pinyin.sogou.com/mac/)，~~没有模糊音对南方人是一种折磨~~  MacOS 13.3 自带输入法也有模糊音了 。其实[百度输入法](https://srf.baidu.com/input/mac.html) 也可以，但是已经用惯搜狗

2. vpn：目前用[红星加速器](https://rocketv.org/index.php/download/) ，含安卓和iOS客户端

3. [Chrome](https://www.google.com/chrome/) (下载比较慢), [Edge](https://www.microsoft.com/en-us/edge/download?form=MA13FJ), [Firefox](https://www.mozilla.org/en-US/firefox/mac/) 装这么多浏览器有一个很现实目的，medium.com 上的付费文章，一个浏览器，一个月只能读三篇。

4. [VLC 播放器](https://www.videolan.org/vlc/download-macosx.html)：以前还有MPlayerX 但它很久不更新,所以只有VLC可选了

5. [金山 office](https://mac.wps.cn/)， 如果不想用盗版office，金山office是唯一选择了。能完美打开office，苹果的pages和numbers都不行

6. [网易云音乐](https://music.163.com/#/download)， https://demo.unlock-music.dev/ 解锁 （需要VPN）

7. [微信](https://mac.weixin.qq.com/) 或者Mac Store

8. [Hazel](https://www.noodlesoft.com/) 神器，不过40美金太贵了，我唯一用的破解版

9. 网盘，说不清到底哪个好用：[百度](https://pan.baidu.com/download#pan) 或 [OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/download) 还是 [阿里aDrive](https://www.aliyundrive.com/) 。但都那他们下过，百度应该还是用得最多的；dropbox被墙没法用

10. [Skype](https://www.skype.com/en/get-skype/) 因为有几个skype朋友，一直有联系

11. ~~[Skitch](https://evernote.com/intl/zh-cn/products/skitch) 圈点~~ 自从知道 preview怎么截图后就不用它了

12. [XnViewMP](https://www.xnview.com/en/xnviewmp/)， 可选的photo viewer不多。因为XnViewMP UI实在不好，太像一个Windows 应用，我现在用Picsee (Mac商店下载)多些，国人软件支持一下！但是Picsee不方便浏览目录，[这个问题我给作者开了问题单，作者确认](https://github.com/kzhiquan/Picsee/issues/36)，希望以后能改进。所以目前这两个工具都用。

13. [迅雷](https://mac.xunlei.com/)，因为经常下电影

14. ~~[The Unarchiver](https://theunarchiver.com/) 用来解压rar （因为rar最早是window专有的）~~，但现在发现 **Unzip One** 更好用（Mac Store），还能先看文件内容

15. Page ，但基本只用markdown

16. iMove 偶尔做下视频编辑

17. 笔记终于改用  **Notion** (Mac Store)。我从2011年就开始用 [印象笔记](https://staging.yinxiang.com/download/)，但之后它不停作妖，比如免费版就只能两台设备。2021年底为了这个原因还买了一年使用权，发现不值。但因为有过去近10年写的笔记，一直没换；这几年也考察几个别的笔记，比如有道云笔记，微软One Note 但都没换成。这次实在受不了印象笔记了，下定决心换一条一条拷贝到Notion.

18. youtube 视频下载器 [open video downloader](https://github.com/StefanLobbenmeier/youtube-dl-gui) 要用这个版本，官方版已经失效了，但是这个非官方版有个bug，必要的插件经常下不下来，而且不给提示，结果就造成没法下载了 [stuck at "Downloading metadata..." for 4.9 & 4.10](https://github.com/StefanLobbenmeier/youtube-dl-gui/issues/51) 所以当一个版本能用之后不要轻易升级，因为升级就要再下载一次所有插件，很容易下载失败。

19. [HandBrake](https://handbrake.fr/downloads.php) 压缩各种格式视频成mp4 方便在手机观看

20. Kindle (Mac Store) 有点鸡肋，但还是每次都装了

21. Finder 替代品，比如方便显示隐藏文件，方便文件拷贝、移动。目前用 [commander one](https://mac.eltima.com/file-manager.html) , 它最明显的功能就是两个pane方便拷贝移动文件。不过就我个人经验，10年前 Finder功能确实弱了一点，需要找一些它的替代品。但现在也勉强能用了，所以用它替代品的机会就少了不少，比如说我想不出花40美金买[Finder Path](https://www.cocoatech.io/) 的理由！

22. https://www.devontechnologies.com/apps/freeware 比如 easyfind 查找文件，毕竟 find命令有点复杂

    

### 开发相关

1. [vscode](https://code.visualstudio.com/download) (官网下载很慢，需要开vpn)：它的插件找在下面总结
2. [Typora](https://typora.io/)：个人觉得最好用的md编辑器 , 我一共买了三个license 
3. [BBEdit 文本编辑器](https://www.barebones.com/support/bbedit/updates.html),也是开发人员必备, 更不用说我在2019年花了30美金买了正版 bbedit 13.5.7，在2023.6.13再次话30美金升级到14.6.6
4. [SourceTree](https://www.sourcetreeapp.com/) 版本管理, [设置github账号的ssh 访问](https://docs.github.com/en/github/authenticating-to-github/testing-your-ssh-connection) 或者[personal access token](https://github.com/settings/tokens) 但是 clone项目出错，原因还在查, 而且 github.com Access Key for qiulang2000 的密码，用 原来github生成的pat也显示错误。
5. [iTerm2](https://iterm2.com/) + [fig](https://fig.io/) (需要在系统设置里允许 自动补全) 现在用 **warp** 多
6. 因为不做iOS开发了就不需要 xcode，只需要Command Line Tools (CLT) for Xcode: `xcode-select --install`  这个装Homebrew就需要
7. [Homebrew](https://brew.sh/), 安装被墙，设置国内代理也麻烦，虽然我给他提了[问题单](https://github.com/Homebrew/brew/issues/6640)，他也修改了。 所以我现在 **弃用 homebrew 改用[macports](https://www.macports.org/)** （见下面描述） + macport list

```shell
==> Tapping homebrew/core
Cloning into '/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core'...
remote: Enumerating objects: 442, done.
remote: Counting objects: 100% (442/442), done.
remote: Compressing objects: 100% (189/189), done.
error: RPC failed; curl 18 transfer closed with outstanding read data remaining
fatal: the remote end hung up unexpectedly
fatal: early EOF
fatal: index-pack failed
Error: Failure while executing; `git clone https://github.com/Homebrew/homebrew-core /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core` exited with 128.
Error: Failure while executing; `/usr/local/bin/brew tap homebrew/core` exited with 1.
Failed during: /usr/local/bin/brew update --force
```

反复执行几次成功了，可能还是跟翻墙后的网速有问题

7. ~~Go2Shell, macOS12 不起作用了~~，改用 https://github.com/Breathleas/Go2Shell, **再有新机器就用** https://github.com/Ji4n1ng/OpenInTerminal 也还不错。

8. 做开发当然需要diff 工具，没有感觉那个特别好只能推荐，就不列了. 目前基本就用bbedit 提供diff

9. Python + [miniconda](https://docs.conda.io/en/latest/miniconda.html) + pip list

   ```
   pip list
   Package                Version
   ---------------------- ---------
   autopep8               1.6.0
   certifi                2021.10.8
   charset-normalizer     2.0.12
   Deprecated             1.2.13
   idna                   3.3
   importlib-resources    5.4.0
   mysql-connector-python 8.0.31
   packaging              21.3
   pexpect                4.8.0
   Pillow                 9.2.0
   pip                    22.3
   protobuf               3.20.1
   ptyprocess             0.7.0
   pycodestyle            2.8.0
   pyparsing              3.0.7
   redis                  4.1.4
   requests               2.27.1
   setuptools             58.1.0
   termcolor              1.1.0
   toml                   0.10.2
   urllib3                1.26.8
   wrapt                  1.14.0
   yachalk                0.1.5
   ```

   

10. nodejs （工作相关）+ npm list 

    ```
    npm ls -g
    /usr/local/lib
    ├── artillery@2.0.0-30
    ├── corepack@0.10.0
    ├── http-server@14.1.1
    ├── n@8.0.2
    ├── npm@8.15.1
    ├── qnm@2.6.0
    ├── typescript@4.6.2
    └── yarn@1.22.17
    ```

    

11. redis 客户端 花钱买了正版的 medis 2; redis自家出的 [RedisInsight-v2](https://redis.com/redis-enterprise/redis-insight/)

12. [Fiddler Everywhere](https://www.telerik.com/download/fiddler-everywhere)单位买了正版

13. 腾讯会议，qq 上班要用，工作上的沟通

14. mysql 客户端 TablePlus 免费版功能受限， sequel-pro 比较丑陋，但能用

15. 因为用 m1 芯片，用docker意义不是很大，可装可不装

16. JetBrains 难免会装一些

17. [Stats](https://github.com/exelban/stats)

18. ~~[cursor.so](https://www.cursor.so/)~~ github copilot chat




有一点教训，通过硬盘拷贝源代码，git 总是会认为所有文件都有修改，可能是因为FAT32文件系统的原因，直接airdrop 其实还挺快。

#### vscode 插件

[How can you export the Visual Studio Code extension list?](https://stackoverflow.com/questions/35773299/how-can-you-export-the-visual-studio-code-extension-list)

[Export/Import VS extensions list?](https://stackoverflow.com/questions/46235923/export-import-vs-extensions-list)

列出的插件太多有些其实没真的用，确实在用有这些

1. Git Extension Pack
2. Git History 这两个git 插件其实都是因为 GitLens — Git supercharged 要收费了
3. GitHub Theme
4. GitHub Copilot
5. GitHub Copilot Labs
6. Prettier - Code formatter 还必须设置vscode 缺省的formatter https://www.alphr.com/use-prettier-vs-code/
7. Python
8. Python Extension Pack 它会再安装其他python插件
9. Todo Tree
10. ESlint
11. Javascript Debugger
12. Vue Language Features (Volar)
13. Vetur
14. Json
15. Fig 会被自动安装

```
code --list-extensions
aaron-bond.better-comments
albert.TabOut
alefragnani.project-manager
batisteo.vscode-django
codezombiech.gitignore
dbaeumer.vscode-eslint
donjayamanne.git-extension-pack
donjayamanne.githistory
donjayamanne.python-environment-manager
donjayamanne.python-extension-pack
eamodio.gitlens
Equinusocio.vsc-community-material-theme
esbenp.prettier-vscode
GitHub.copilot
GitHub.copilot-labs
GitHub.github-vscode-theme
github.vscode-github-actions
Gruntfuggly.todo-tree
KevinRose.vsc-python-indent
ms-azuretools.vscode-docker
MS-CEINTL.vscode-language-pack-zh-hans
ms-python.isort
ms-python.python
ms-python.vscode-pylance
ms-toolsai.jupyter
ms-toolsai.jupyter-keymap
ms-toolsai.jupyter-renderers
ms-toolsai.vscode-jupyter-cell-tags
ms-toolsai.vscode-jupyter-slideshow
ms-vscode-remote.remote-containers
ms-vscode.cmake-tools
ms-vscode.cpptools
ms-vscode.cpptools-extension-pack
ms-vscode.cpptools-themes
ms-vscode.js-debug-nightly
njpwerner.autodocstring
octref.vetur
PKief.material-icon-theme
twxs.cmake
VisualStudioExptTeam.intellicode-api-usage-examples
VisualStudioExptTeam.vscodeintellicode
Vue.volar
wholroyd.jinja
withfig.fig
ZainChen.json
ziyasal.vscode-open-in-github
```



#### MacPorts 安装过的插件

[See what has been installed via MacPorts](https://stackoverflow.com/questions/9191737/see-what-has-been-installed-via-macports)

有印象是 **the_silver_searcher**/tree/tmux/sqlite3/redis (会顺带安装)/zlib/httpie（会顺带安装python 3.8）/wget  

macpors会 生产**joshua root** 后台进程

ag/redis 必装

```
port installed
Warning: port definitions are more than two weeks old, consider updating them by running 'port selfupdate'.
The following ports are currently installed:
  bzip2 @1.0.8_0 (active)
  curl-ca-bundle @7.82.0_0 (active)
  expat @2.4.7_0 (active)
  gettext @0.21_0 (active)
  gettext-runtime @0.21_0 (active)
  gettext-tools-libs @0.21_0 (active)
  gmp @6.2.1_0 (active)
  gnutls @3.6.16_3 (active)
  htop @3.1.2_0 (active)
  httpie @3.1.0_0+python38 (active)
  icu @67.1_4 (active)
  libedit @20210910-3.1_1 (active)
  libevent @2.1.12_1 (active)
  libffi @3.4.2_2 (active)
  libiconv @1.16_1 (active)
  libidn2 @2.3.2_1 (active)
  libpsl @0.21.1-20210726_2 (active)
  libtasn1 @4.18.0_0 (active)
  libtextstyle @0.21_0 (active)
  libunistring @1.0_0 (active)
  libxml2 @2.9.13_0 (active)
  libxslt @1.1.34_6 (active)
  lrzsz @0.12.20_4 (active)
  ncurses @6.3_0 (active)
  nettle @3.7.3_0 (active)
  openssl @3_2 (active)
  openssl3 @3.0.1_0+legacy (active)
  p11-kit @0.24.1_0 (active)
  pcre @8.45_0 (active)
  pcre2 @10.39_0 (active)
  pkgconfig @0.29.2_0 (active)
  py38-certifi @2021.10.8_0 (active)
  py38-charset-normalizer @2.0.12_0 (active)
  py38-defusedxml @0.7.1_0 (active)
  py38-idna @3.3_0 (active)
  py38-multidict @6.0.2_0 (active)
  py38-pygments @2.12.0_0 (active)
  py38-requests @2.27.1_0 (active)
  py38-requests-toolbelt @0.9.1_0 (active)
  py38-setuptools @62.1.0_0 (active)
  py38-socks @1.7.0_0 (active)
  py38-urllib3 @1.26.9_0 (active)
  pygments_select @0.1_0 (active)
  python3_select @0.0_2 (active)
  python38 @3.8.13_0+optimizations (active)
  python_select @0.3_9 (active)
  redis @6.2.6_1 (active)
  sqlite3 @3.38.1_0 (active)
  sshpass @1.09_0 (active)
  the_silver_searcher @2.2.0_0 (active)
  tmux @3.2a_0 (active)
  tree @1.8.0_0 (active)
  wget @1.21.3_0+gnutls (active)
  xz @5.2.5_0 (active)
  zlib @1.2.11_0 (active)
```

 

#### 2022.3.13 brew安装失败经历

nodejs 16, `npm i -g n`, `n 14`因为用16 带的npm 8.x 安装`node_modules`失败

```
qiulang@qiulangdeMacBook-Air ws_redis % npm list -g --depth=0
/usr/local/lib
├── corepack@0.10.0
├── n@8.0.2
├── npm@6.14.16
├── typescript@4.6.2
└── yarn@1.22.17
```



brew 设置清华镜像源，但是第一次安装也不成功，之后虽然提示成功，但是tap设置不对，什么包都没找到，所以这次干脆试了MacPort，用MacPorts至少一次安装成功。 https://apple.stackexchange.com/questions/32724/what-are-pros-and-cons-for-macports-fink-and-homebrew

```
==> Installation successful!

==> Homebrew has enabled anonymous aggregate formulae and cask analytics.
Read the analytics documentation (and how to opt-out) here:
  https://docs.brew.sh/Analytics
No analytics data has been sent yet (nor will any be during this install run).

==> Homebrew is run entirely by unpaid volunteers. Please consider donating:
  https://github.com/Homebrew/brew#donations

==> Next steps:
- Run these two commands in your terminal to add Homebrew to your PATH:
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/qiulang/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
- Run these commands in your terminal to add the non-default Git remotes for Homebrew/brew and Homebrew/homebrew-core:
    echo 'export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"' >> /Users/qiulang/.zprofile
    echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"' >> /Users/qiulang/.zprofile
    export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
    export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
    
qiulang@qiulangdeMacBook-Air redis % brew info wget
Error: No available formula with the name "wget".
==> Searching for a previously deleted formula (in the last month)...
Error: No previously deleted formula found.
qiulang@qiulangdeMacBook-Air redis % brew info redis
Error: No available formula with the name "redis".
==> Searching for a previously deleted formula (in the last month)...
Error: No previously deleted formula found.

rm -rf "/opt/homebrew/Library/Taps/homebrew/homebrew-core"
brew tap homebrew/core    
https://github.com/Homebrew/homebrew-core/issues/37724
https://github.com/homebrew/install
```



