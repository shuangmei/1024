# -*- coding: utf-8 -*-#
import time

#------------------------------------
# Name:         getDate
# Description:
# Author:       wangjx
# Date:         2022/09/22
#------------------------------------

def getDate():
    return time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())