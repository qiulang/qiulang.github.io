## Mac 装机必备

每次装机都至少要花一两天时间，而且把之前写的装机必备做些更新，这是2020-7-20的版本

### 基础软件

1. 输入法： 搜狗，没有模糊音对南方人是一种折磨
2. vpn：不能用Google对地球人是一种折磨，目前用BetaVPN
3. Chrome
4. VLC 播放器：以前还有MPlayerX 但它很久不更新,所以只有VLC可选了
5. 金山 office， 如果不想用盗版office，金山office是唯一选择了。能完美打开office，苹果的pages和numbers都不行
7. 网易云音乐
9. 微信
10. 网盘，但到底哪个好用实在也说不清，百度还是OneDrive；dropbox被墙没法用
10. Skype 因为有几个skype朋友，一直有联系
11. Skitch 圈点
12. XnViewMP， 可选的photo viewer不多
13. 迅雷
14. [The Unarchiver](https://theunarchiver.com/)
15. Page 勉强装一个吧，虽然我基本只用markdown
15. iMove 偶尔做下视频编辑
16. 印象笔记，其实很烦它，免费版就只能两台设备，但因为有过去几年写的笔记，只能忍着

### 开发相关

1. vscode：它的插件找机会再总结
2. Typora：个人觉得最好用md编辑器  
3. BBEdit 文本编辑器,也是开发人员必备, 更不用说我买了正版!
4. SourceTree 版本管理, [设置github账号](https://docs.github.com/en/github/authenticating-to-github/testing-your-ssh-connection)
5. iTerm2
6. Homebrew, 安装被墙，最简单方法设置vpn `export https_proxy=http://127.0.0.1:2020 http_proxy=http://127.0.0.1:2020 all_proxy=socks5://127.0.0.1:2020`

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

7. Go2Shell

8. 因为不做iOS开发了就不需要 xcode，只需要Command Line Tools (CLT) for Xcode: `xcode-select --install`  这个装Homebrew就需要

9. 做开发当然需要diff 工具，没有感觉那个特别好只能推荐，就不列了

   

