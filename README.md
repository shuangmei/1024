# 1024 邀请码注册脚本 ，最多支持4位掩码

因为一直抢不到邀请码，所以写了一个脚本用来获取邀请码。
最近草榴有大佬每天发10个邀请码，发码如下，
    00fda+cd9+71dc00 或  +da211eb+c4dd1*d 
    
    规则是:
    碼中字母只可能是 abcdef  [16進制規則限制]。
      文本發碼：①、+ 是数字；②、 * 是字母；③、? 是字母或數字。
　  截圖發碼：數字/字母隨機。

他这种发码，手动去遍历抢码基本上是抢不到，因为同样有大佬是写代码去破解。
所以针对这种发码我也写了一个自动抢码脚本，同时也可以验证识别码

## 安装python环境
需要安装python3 环境， 最好是3.8以上的环境
同时需要安装python 如 yaml 、prestool 、 urllib3 、 requests 等库
```
pip install pyyaml
pip install prestool
pip install requests
pip install urllib3
```


## 注册超级鹰账号并充值
因为之前想用百度的OCR识别，但是百度的OCR识别草榴的验证码成功率太低了，所以找到了超级鹰，这个识别率相当的高。

注册地址： http://www.chaojiying.com/

## 申请软件ID
注册账号并成功登录后， 
访问 http://www.chaojiying.com/user/mysoft/
然后 生成一个软件ID 这里的软件ID 就是后面配置文件里需要的信息


## 修改配置文件 
在conf目录下有一个config.yaml, 按照注释的提示，将中文文字修改为你想
要填写的内容, 
 "+" 、 "*" 、 "？" 这三个是发码人的规则，根据发码人的规则进行修改


```
# -*- coding: UTF-8 -*-#
#------------------------------------
# Name:         config
# Description:
# Author:       wangjx
# Date:         2022/09/22
#------------------------------------

#---------邀请码掩码规格-------
# + 号代表哪些数字或字母
jiahao: 0123456789
# * 号代表哪些数字或字母
xinghao: abcdef
# ？ 号代表哪些数字或字母
wenhao: 0123456789abcdef

#---------超级鹰相关信息-------
# 账号
user: 超级鹰账号
# 密码
pass2: 超级鹰密码
# appID
softid: 超级鹰应用ID

#---------注册草榴账号信息-------
#用户名
regname: 注册用户名
#密码
regpwd: 注册密码
#邮箱
regemail: 注册邮箱


# 常规配置信息， 草榴地址和验证码地址

url: https://www.t66y.com/register.php?
# url:  https://cl.9602x.xyz/register.php?
validateUrl: https://www.t66y.com/require/codeimg.php?0.
# validateUrl:  https://cl.9602x.xyz/require/codeimg.php?0.

#执行的序号
index: 0

#要破解的邀请码
code ： '*da211eb*c4dd1*d'
```
以上的配置文件会在运行没有注释了，请大家注意一下。


## 运行
进入main.py所在的目录
执行下面的命令运行脚本
```
python main.py  
```

## 增加了断网或执行时卡住了，再次重新执行脚本时，可以接着破解的功能

如果想换一个新的，就将 code 修改一下 然后 把conf\config.yaml里的
```angular2html
index: ？
```

这里的 ？ 修改为 0 即可，表示从头开始 如果不为0 表示接着执行，
一般情况下， 修改为 0 即可


```angular2html
reg.forCheckCode(codeList, 0, code)
改为
reg.forCheckCode(codeList, 220, code)
```

## 注意事项
1.  get1024Code.py 里的 cookie  建议修改为你们电脑上的，不要使用我这里的提供的cookie 
容易导致注册的账号被禁用
```angular2html

headers 里的

'Cookie': "227c9_ipfrom=7bad9dd8b54d6492055fd5fb17ceebfe%09%C3%C0%B9%FA%B5%C2%BF%CB%C8%F8%CB%B9%D6%DD; 227c9_postReplyLastData=52898511024; PHPSESSID=b5du61ech524gbalm310midvo1; 227c9_lastvisit=0%091663771232%09%2Fregister.php%3F",

headers1 里的

'Cookie': "227c9_ipfrom=7bad9dd8b54d6492055fd5fb17ceebfe%09%C3%C0%B9%FA%B5%C2%BF%CB%C8%F8%CB%B9%D6%DD; 227c9_postReplyLastData=52898511024; PHPSESSID=b5du61ech524gbalm310midvo1; 227c9_lastvisit=0%091663771232%09%2Fregister.php%3F",


```
其实这两个headers 是可以合并的，之前测试过，只用headers 就可以


## 随手写的，很是粗糙，请见谅

