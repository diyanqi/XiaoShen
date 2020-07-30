# XiaoShen
小神AI——一个轻量化基于Python的社区自动回复系统

使用指南： https://blog.amazingcode.top/xiaoshen/

## 安装教程
1.Windows环境安装
- 教程视频： https://www.bilibili.com/video/bv11f4y1X7E9
- 先下载，选择“Download ZIP”。
- 耐心等待下载完成。
- 解压文件夹，并打开目录下的5个.py文件（推荐使用VSCode或Sublime）。
- 众所周知，你的自动回复机器人需要一个编程猫账号。
- 打开浏览器（推荐使用chrome或edge），进入 shequ.codemao.cn，并登录进去。
- 待登陆完成，随便打开一个帖子，如 https://shequ.codemao.cn/community/324839 。
- 此时，按下F12（或者CTRL+shift+I），你会看到弹出了一个开发人员工具。
- 找到开发人员工具窗口上方的选项卡的“网络”，点击进去。
- 继续在左方的界面里回复帖子，随便回复什么。
- 按下“发表回帖”。
- 你会看见“网络”选项卡中多出了几个条目。
- 点击“replies”的条目，有会弹出一个小窗口。
- 找到窗口中的“请求标头”（Request Headers）。
- 找到请求标头中的“Cookie:”，选择并复制后面的一大长串字符串（注意不要复制进头上的空格）。
- 回到打开的5个.py文件。
- 找到每个文件前面几行有一个“mycookie='你的cookie'”的语句。
- 将“mycookie='你的cookie'”中“你的cookie”改成刚才复制下来的一长串字符串，注意：只替换“你的cookie”，不要把单引号替换掉；每一个文件都要这么操作。
- 将这5个.py文件都保存。
- 回到主文件夹，打开“小神”快捷方式。
- 成功运行！
