# -*- coding: UTF-8 -*-#
# ------------------------------------
# Name:        main
# Description:  
# Author:       wangjx
# Date:         2022/09/22
# ------------------------------------

from prestool.Tool import Tool
import common.get1024Code

from common.writeLog import writeLog
import common.getMaskNum
from common.rwyaml import read_yaml, write_yaml

if __name__ == '__main__':

    code = read_yaml('code')
    writeLog('code is :{}'.format(code))

    tool = Tool()

    maskList = common.getMaskNum.getMasklist(code)
    charsList = common.getMaskNum.getChars(maskList)

    if len(maskList) <= 4:
        url = read_yaml('url')
        print(url)
        validateUrl = read_yaml('validateUrl') + tool.random_number(16)
        reg = common.get1024Code.CodeSearch1024(code, url, validateUrl, charsList[0], charsList[1], charsList[2],
                                                charsList[3], 0, 0, 0, 0)
        codeList = reg.start(False)
        reg.forCheckCode(codeList, read_yaml('index'), code)

    else:
        writeLog('不能处理大于4个隐藏字符的邀请码')
