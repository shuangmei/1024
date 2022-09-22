# -*- coding: utf-8 -*-#

#------------------------------------
# Name:         writeLog
# Description:  
# Author:       wangjx
# Date:         2022/09/22
#------------------------------------

import time
from common.getDate import getDate


def writeLog(content):
    print(getDate()+':'+str(content))
    f1 = open('logs/cl1024_'+time.strftime('%Y-%m-%d', time.localtime())+'.log', 'a+')
    f1.write(getDate()+':'+str(content)+'\n')
    f1.close()