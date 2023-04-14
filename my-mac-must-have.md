## Mac 装机必备

每次装机都至少要花一两天时间，而且把之前写的装机必备做些更新，这是2023-3-24的版本。我分成两大类，日常使用和开发使用

### 基础软件

1. 输入法： [搜狗](https://pinyin.sogou.com/mac/)，没有模糊音对南方人是一种折磨。其实[百度输入法](https://srf.baidu.com/input/mac.html) 也可以，但是已经用惯搜狗

2. vpn：不能用Google对地球人是一种折磨，更别说现在还要ChatGPT. 目前用[红星加速器](https://rocketv.org/index.php/download/) (含安卓客户端) + 公司的 Cisco Anyconnect

3. [Chrome](https://www.google.com/chrome/), [Edge](https://www.microsoft.com/en-us/edge/download?form=MA13FJ), [Firefox](https://www.mozilla.org/en-US/firefox/mac/) 装这么多浏览器有一个很现实目的，medium.com 上的付费文章，一个浏览器，一个月只能读三篇。

4. [VLC 播放器](https://www.videolan.org/vlc/download-macosx.html)：以前还有MPlayerX 但它很久不更新,所以只有VLC可选了

5. [金山 office](https://mac.wps.cn/)， 如果不想用盗版office，金山office是唯一选择了。能完美打开office，苹果的pages和numbers都不行

6. [网易云音乐](https://music.163.com/#/download)， https://demo.unlock-music.dev/ 解锁

7. [微信](https://mac.weixin.qq.com/) 或者Mac Store

8. [Hazel](https://www.noodlesoft.com/) 神器，不过40美金太贵了，我唯一用的破解版

9. 网盘，说不清到底哪个好用：[百度](https://pan.baidu.com/download#pan) 或 [OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/download) 还是 [阿里aDrive](https://www.aliyundrive.com/) 。但都那他们下过，百度应该还是用得最多的；dropbox被墙没法用

10. [Skype](https://www.skype.com/en/get-skype/) 因为有几个skype朋友，一直有联系

11. [Skitch](https://evernote.com/intl/zh-cn/products/skitch) 圈点

12. [XnViewMP](https://www.xnview.com/en/xnviewmp/)， 可选的photo viewer不多，但因为XnViewMP UI实在不好，太像一个Windows 应用，我现在改用Picsee (Mac商店下载)，国人软件支持一下！

13. [迅雷](https://mac.xunlei.com/)，因为经常下电影

14. ~~[The Unarchiver](https://theunarchiver.com/) 用来解压rar （因为rar最早是window专有的）~~，但现在发现 **Unzip One** 更好用（Mac Store），还能先看文件内容

15. Page ，但基本只用markdown

16. iMove 偶尔做下视频编辑

17. 笔记终于改用  **Notion** (Mac Store)。我从2011年就开始用 [印象笔记](https://staging.yinxiang.com/download/)，但之后它不停作妖，比如免费版就只能两台设备。2021年底为了这个原因还买了一年使用权，发现不值。但因为有过去近10年写的笔记，一直没换；这几年也考察几个别的笔记，比如有道云笔记，微软One Note 但都没换成。这次实在受不了印象笔记了，下定决心换一条一条拷贝到Notion.

18. youtube 视频下载器 [open video downloader](https://github.com/StefanLobbenmeier/youtube-dl-gui) 要用这个版本，官方版已经失效了

19. [HandBrake](https://handbrake.fr/downloads.php) 压缩各种格式视频成mp4 方便在手机观看

20. Kindle (Mac Store) 有点鸡肋，但还是每次都装了

21. Finder 替代品，比如方便显示隐藏文件，方便文件拷贝、移动。目前用 [commander one](https://mac.eltima.com/file-manager.html) , 它最明显的功能就是两个pane方便拷贝移动文件。不过就我个人经验，10年前 Finder功能确实弱了一点，需要找一些它的替代品。但现在也勉强能用了，所以用它替代品的机会就少了不少，比如说我想不出花40美金买[Finder Path](https://www.cocoatech.io/)

    

### 开发相关

1. [vscode](https://code.visualstudio.com/download)：它的插件找机会再总结
2. [Typora](https://typora.io/)：个人觉得最好用md编辑器 , 我一共买了三个license 
3. [BBEdit 文本编辑器](https://www.barebones.com/support/bbedit/updates.html),也是开发人员必备, 更不用说我花了30美金买了正版 bbedit 13.5.7
4. [SourceTree](https://www.sourcetreeapp.com/) 版本管理, [设置github账号](https://docs.github.com/en/github/authenticating-to-github/testing-your-ssh-connection)
5. [iTerm2](https://iterm2.com/) + [fig](https://fig.io/)
6. 因为不做iOS开发了就不需要 xcode，只需要Command Line Tools (CLT) for Xcode: `xcode-select --install`  这个装Homebrew就需要
7. [Homebrew](https://brew.sh/), 安装被墙，设置国内代理也麻烦，虽然我给他提了[问题单](https://github.com/Homebrew/brew/issues/6640)，他也修改了。 所以我现在 **弃用 homebrew 改用[macport](https://www.macports.org/)** （见下面描述）

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

9. 做开发当然需要diff 工具，没有感觉那个特别好只能推荐，就不列了. 目前基本就用bbedit 提供diff

10. Python + [miniconda](https://docs.conda.io/en/latest/miniconda.html)

11. nodejs （工作相关）

12. redis 客户端 花钱买了正版的 medis 2; redis自家出的 [RedisInsight-v2](https://redis.com/redis-enterprise/redis-insight/)

13. [Fiddler Everywhere](https://www.telerik.com/download/fiddler-everywhere)单位买了正版

14. 腾讯会议，qq 上班要用，工作上的沟通

15. mysql 客户端 TablePlus 免费版功能受限， sequel-pro 比较丑陋，但能用

16. 因为用 m1 芯片，用docker意义不是很大，可装可不装

17. JetBrains 难免会装一些

18. [Stats](https://github.com/exelban/stats)

    

#### 2022.3.13

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



