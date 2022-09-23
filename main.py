# -*- coding: UTF-8 -*-#
#------------------------------------
# Name:        main
# Description:  
# Author:       wangjx
# Date:         2022/09/22
#------------------------------------

from prestool.Tool import Tool
import common.get1024Code

from common.writeLog import writeLog
import common.getMaskNum 
import yaml
    
if __name__ == '__main__':
    
    
    code = '00fda+cd9+71dc00'
    writeLog('code is :{}'.format(code))
    
    # 读取配置文件(config.yaml)
    with open('conf/config.yaml') as yfile:
        try:
            yobj = yaml.safe_load(yfile)
        except yaml.YAMLError as error:
            print(error)

    tool = Tool()
    
    maskList = common.getMaskNum.getMasklist(code)
    charsList = common.getMaskNum.getChars(maskList)
    
    if(len(maskList) <=4 ):
        url = yobj.get('url')
        validateUrl = yobj.get('validateUrl') +  tool.random_number(16)
        reg = common.get1024Code.CodeSearch1024(code, url, validateUrl, charsList[0], charsList[1], charsList[2], charsList[3], 0, 0, 0, 0)
        codeList = reg.start(False)
        reg.forCheckCode(codeList, 0, code)



    else:
        writeLog('不能处理大于4个隐藏字符的邀请码')