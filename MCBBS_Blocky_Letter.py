# -*- coding: UTF-8 -*-
#Author: ETW_Zero
#功能：填写下面的变量，运行该脚本，即可生成慢讯源代码，粘贴到源代码编辑器就可以辣
#虽然，不推荐变量名称中使用中文，但是在填写的时候确实挺舒服的（
#模板来自@kakagou的帖子： https://www.mcbbs.net/thread-1201529-1-1.html ，卡狗大大太强辣

import re
#import pyperclip #你可以选择使用pyperclip直接获得快讯的源代码，发帖的时候直接粘贴就可以了
'''
#大概不会更改的地方
君の名は = ''
#需要准备的图片
头像图片地址 = ''
配图链接 = ''
#需要获取的信息
用户昵称 = ''
用户唯一标识符 = ''
正文 = ''
译文 = ''
原文地址 = ''
推文发布时间 = ''
'''
#大概不会更改的地方
君の名は = 'ETW_Derp'
#需要准备的图片
头像图片地址 = ''
配图链接 = ''
#需要获取的信息
用户昵称 = ''
用户唯一标识符 = ''#即用户名，比如@kingbdogz
正文 = ''#超链接记得前后带空格，将 https:// 也带上
译文 = ''#超链接记得前后带空格，将 https:// 也带上
原文地址 = ''
推文发布时间 = ''

#Done(_Todo: 正文添加蓝色链接的正则表达式_)
Template = '[align=center][table=560,#FFFFFF]\n\
[tr][td][font=-apple-system, BlinkMacSystemFont,Segoe UI, Roboto, Helvetica, Arial, sans-serif][indent]\n\
[float=left][img=44,44]'+头像图片地址+'[/img][/float][size=15px][b][color=#0F1419]'+用户昵称+'[/color][/b]\n\
[color=#5B7083]'+用户唯一标识符+'[/color][/size]\n\
\n\
[color=#0F1419][size=23px]'+正文+  '''[color=#1B95E0]蓝色链接[/color]正文'''  '[/size]\n\
[size=15px]由 '+君の名は+' 翻译自 英语[/size]\n\
[size=23px]'+译文+'[/size][/color][/indent][align=center][img=451,254]'+配图链接+'[/img][/align][indent][size=15px][url='+原文地址+'][color=#5B7083]'+推文发布时间+'[/color][/url][/size][/indent][/font]\n\
[/td][/tr]\n\
[/table][/align]\n\
\n\
'

HTTPRE = r'([a-zA-z]+://[^\s]*)'
正文 = re.sub(HTTPRE, r'[color=#1B95E0]\1', 正文)#自动为所有超链接添加颜色，下同
正文 = re.sub(HTTPRE, r'\1[/color]', 正文)
译文 = re.sub(HTTPRE, r'[color=#1B95E0]\1', 译文)
译文 = re.sub(HTTPRE, r'\1[/color]', 译文)
print(Template)
#pyperclip.copy(Template)
'''
填写示例：
[align=center][table=560,#FFFFFF]
[tr][td][indent][font=-apple-system, BlinkMacSystemFont,Segoe UI, Roboto, Helvetica, Arial, sans-serif]
[float=left][img=44,44]https://attachment.mcbbs.net/data/myattachment/forum/202105/17/145006gcwbcuzwmue0wgwk.png[/img][/float][size=15px][b][color=#0F1419]Henrik Kniberg[/color][/b]
[color=#5B7083]@henrikkniberg[/color][/size]

[size=23px][color=#0F1419]We made large ore veins slightly more rare and slightly smaller on average. The sizes vary a lot so you can still find megaveins once in a while. As always, test in survival mode and give us feedback! Use the C&C preview datapack.[/color][/size]
[size=15px]由 dwch 翻译自英语[/size]
[size=23px][color=#0F1419]大矿脉会变得稍微更稀有一些，而且平均下来大小也稍微小一些。矿脉大小分布很广，仍然有可能找到贼拉大的矿脉。请在生存模式中加以测试，并给予我们反馈！使用最新的预览版数据包即可体验。[/color][/size][/font][/indent][align=center][media=x,500,375]https://www.bilibili.com/video/av587880250[/media][/align][indent][size=15px][url=https://twitter.com/henrikkniberg/status/1389979425501061129][color=#5B7083]上午12:24 · 2021年5月6日·Twitter Web App[/color][/url][/size][/indent]
[/td][/tr]
[/table][/align]
'''