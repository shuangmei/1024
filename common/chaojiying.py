# -*- coding: UTF-8 -*-#

#------------------------------------
# Name:         chaojiying
# Description:  
# Author:       wangjx
# Date:         2022/09/22
#------------------------------------

from hashlib import md5
from prestool.Tool import Tool
import time
import requests
from lxml import etree
import random
from urllib import request
import urllib3

from common.getDate import getDate
from common.writeLog import writeLog
import yaml

urllib3.disable_warnings()

class Chaojiying_Client(object):

    def __init__(self):
        
        # 读取配置文件(config.yaml)
        with open('conf/config.yaml') as yfile:
            try:
                yobj = yaml.safe_load(yfile)
            except yaml.YAMLError as error:
                print(error)
        
        self.username = yobj.get('user')
        password = yobj.get('pass2').encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = yobj.get('softid')
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
            'codetype': '1004',
            "len_min": '4'
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post(
            'http://upload.chaojiying.net/Upload/Processing.php',
            data=params,
            files=files,
            headers=self.headers
        )
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post(
            'http://upload.chaojiying.net/Upload/ReportError.php',
            data=params,
            headers=self.headers
        )
        return r.json()
