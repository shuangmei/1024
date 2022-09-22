# -*- coding: utf-8 -*-#
import time

3  #------------------------------------
4  # Name:         getDate
5  # Description:  
6  # Author:       wangjx
7  # Date:         2022/09/22
8  #------------------------------------

def getDate():
    return time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())