# -*- coding: UTF-8 -*-#

#------------------------------------
# Name:         1024草榴
# Description:  
# Author:       wangjx
# Date:         2022/09/22
#------------------------------------


import time
import requests
import random
import urllib3


from common.writeLog import writeLog
import common.chaojiying
from common.rwyaml import read_yaml
from common.rwyaml import write_yaml
urllib3.disable_warnings()


urllib3.disable_warnings()
user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]


def get_user_agent():
    return random.choice(user_agent)


requests.packages.urllib3.disable_warnings()

headers = {
    'Cookie': "227c9_ipfrom=7bad9dd8b54d6492055fd5fb17ceebfe%09%C3%C0%B9%FA%B5%C2%BF%CB%C8%F8%CB%B9%D6%DD; 227c9_postReplyLastData=52898511024; PHPSESSID=b5du61ech524gbalm310midvo1; 227c9_lastvisit=0%091663771232%09%2Fregister.php%3F",
    # 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    'User-Agent': get_user_agent()
}

headers1 = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Cache-Control': "max-age=0",
    'Connection': "keep-alive",
    'Content-Length': "175",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "227c9_ipfrom=7bad9dd8b54d6492055fd5fb17ceebfe%09%C3%C0%B9%FA%B5%C2%BF%CB%C8%F8%CB%B9%D6%DD; 227c9_postReplyLastData=52898511024; PHPSESSID=b5du61ech524gbalm310midvo1; 227c9_lastvisit=0%091663771232%09%2Fregister.php%3F",
    'DNT': "1",
    'Host': "www.t66y.com",
    'Origin': "https://www.t66y.com",
    'Referer': "https://www.t66y.com/register.php",
    'sec-ch-ua': "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': "document",
    'Sec-Fetch-Mode': "navigate",
    'Sec-Fetch-Site': "same-origin",
    'Sec-Fetch-User': "?1",
    'Upgrade-Insecure-Requests': "1",
    # 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    'User-Agent': get_user_agent()
}

class CodeSearch1024():
    def __init__(self, codeWithMask, url, validateUrl, chars, chars1,chars2 ,chars3, index1, index2, index3, index4):
        
        # 读取配置文件(config.yaml)
        
            
        self.url = url
        self.validateUrl = validateUrl
        self.codeWithMask = codeWithMask
        self.chars = chars 
        self.chars1 = chars1
        self.chars2 = chars2
        self.chars3 = chars3
        
        self.chaojiying = common.chaojiying.Chaojiying_Client()  # 用户中心>>软件ID 生成一个替换 96001
        self.indexNum1 = index1
        self.indexNum2 = index2
        self.indexNum3 = index3
        self.indexNum4 = index4


    #根据掩码规则生成验证码list                
    def start(self, samemask=False):
        writeLog('star')
        maskCount = len(common.getMaskNum.getMasklist(self.codeWithMask))
        writeLog('maskCount{} '.format(maskCount))
        self.codeWithMask = self.codeWithMask.replace('*', '%s')
        self.codeWithMask = self.codeWithMask.replace('+', '%s')
        self.codeWithMask = self.codeWithMask.replace('?', '%s')
        
        codeList = []
        
        if maskCount == 0:
            code = self.codeWithMask
            codeList.append(code)
                
        elif samemask: #暂时不用
            for ch in self.chars:
                code = self.codeWithMask % ((ch,) * maskCount)
                codeList.append(code)
                    
        elif maskCount == 1:
            for self.indexNum1 in range(len(self.chars)):
                code = self.codeWithMask % (self.chars[self.indexNum1])
                codeList.append(code)

        elif maskCount == 2:
            for self.indexNum1 in range(len(self.chars)):
                for self.indexNum2 in range(len(self.chars1)):
                    code = self.codeWithMask % (
                        self.chars[self.indexNum1], self.chars1[self.indexNum2])
                    codeList.append(code)

        elif maskCount == 3:
            for self.indexNum1 in range(len(self.chars)):
                for self.indexNum2 in range(len(self.chars1)):
                    for self.indexNum3 in range(len(self.chars2)):
                        code = self.codeWithMask % (
                            self.chars[self.indexNum1], self.chars1[self.indexNum2], self.chars2[self.indexNum3])
                        codeList.append(code)
                        
        
        elif maskCount == 4:
            for self.indexNum1 in range(len(self.chars)):
                for self.indexNum2 in range(len(self.chars1)):
                    for self.indexNum3 in range(len(self.chars2)):
                        for self.indexNum4 in range(len(self.chars3)):
                            code = self.codeWithMask % (
                                self.chars[self.indexNum1], self.chars1[self.indexNum2], self.chars2[self.indexNum3], self.chars3[self.indexNum4])
                            codeList.append(code)
        
        return codeList

    #开始获取验证码
    def getInvCoce(self):
        writeLog('开始获取验证码')
        try:
            while True:
                rsp = requests.get(
                    self.validateUrl,
                    stream=True,
                    headers=headers,
                    verify=False
                )
                with open('a.jpg', 'wb') as fd:
                    for chunk in rsp.iter_content():
                        fd.write(chunk)
                fd.close()
                time.sleep(1)
                writeLog('获取到验证码图片，保存成文件')
                im = open('a.jpg', 'rb').read()
                writeLog('开始识别验证码')
                validate = self.chaojiying.PostPic(im, 1902)
                writeLog('validate json ={} ！'.format(validate))
                validate = str(validate['pic_str']).upper()
                writeLog('得到的验证码 validate:{}'.format(validate))
                if len(validate) >= 4:
                    return validate

        except Exception as e:
            writeLog('出现异常 :{}'.format(e))
            return ""
        
    #请求检测验证码
    def RegUser(self, code):

        validate = self.getInvCoce()
        payload = {
            'regname': read_yaml('regname'),
            'regpwd': read_yaml('regpwd'),
            'regpwdrepeat': read_yaml('regpwd'),
            'regemail': read_yaml('regemail'),
            'invcode': code,
            'validate': validate,
            'forward': '',
            'step': '2'
        }

        r = requests.request(
            "POST",
            self.url,
            headers=headers1,
            data=payload,
            verify=False
        )
        html = r.text
        writeLog('返回数据：{} '.format(html))

    #请求检测验证码
    def checkInvcode(self, code):
        payload = {
            'reginvcode': code,
            'validate': self.getInvCoce(),
            'action': 'reginvcodeck'
        }

        r = requests.request(
            "POST",
            self.url,
            headers=headers,
            data=payload,
            verify=False
        )
        writeLog('返回数据：{} '.format(r.text))
        return r.text

    #开始检测验证码是否有效
    def doReg(self, code, n):
        # 可重试5次
        writeLog('==================================================================================================')
        writeLog('doReg! code {} '.format(code))
        
        try:
            if n > 5:
                return 'timeout'

            html = self.checkInvcode(code)
            if html.find('parent.retmsg_invcode(\'1\')') > -1:
                writeLog('邀請碼不存在或已被使用，您無法注冊！')
                return "None"

            elif html.find('parent.retmsg_invcode(\'2\')') > -1:
                writeLog('驗證碼不正確，請重新填寫!')
                self.doReg(code, n)

            elif html.find('parent.retmsg_invcode(\'0\')') > -1:
                writeLog('恭喜您，您可以使用這個邀請碼註冊！')
                self.RegUser(code)
                return "found"

        except Exception as e:
            return self.doReg(code, n + 1)  # 递归

    #循环验证码list
    def forCheckCode(self, codeList, idx, oldCode):
        while idx < len(codeList):
            writeLog('codeList idx：{} 和 code：{} 原掩码code：{}'.format(idx, codeList[idx], oldCode))
            write_yaml('index', idx)
            result = self.doReg(codeList[idx], 0)
            idx = idx + 1
            if result == 'found':
                writeLog('code{} found！'.format(codeList[idx]))
                return
            else:
                writeLog('code{} result:{} ！'.format(codeList[idx], result))