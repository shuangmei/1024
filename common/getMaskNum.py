# -*- coding: utf-8 -*-#

#------------------------------------
# Name:         getMask
# Description:  
# Author:       wangjx
# Date:         2022/09/22
#------------------------------------

import yaml



def getMasklist(code):
    result =[]
    for ch in code:
        if ch == '*':
            result.append("xh")
        if  ch == "+":
            result.append("jh")
        if  ch == "?":
            result.append("wh")
    return result

def getChars(result):
    charsList =[]
    # 读取配置文件(config.yaml)
    with open('conf/config.yaml') as yfile:
        try:
            yobj = yaml.safe_load(yfile)
        except yaml.YAMLError as error:
            print(error)
                
    jiahao = str(yobj.get('jiahao'))
    xinghao = str(yobj.get('xinghao'))
    wenhao = str(yobj.get('wenhao'))
    
    chars = xinghao
    chars1 = xinghao
    chars2 = xinghao
    chars3 = xinghao
    
    if  (len(result) >=1):
        if result[0] == "xh":
            chars = xinghao      
        elif result[0] == "jh":
            chars = jiahao
        elif result[0] == "wh":
            chars = wenhao
        
        
        
    if (len(result) >= 2):   
        if result[1] == "xh":
            chars1 = xinghao        
        elif result[1] == "jh":
            chars1 = jiahao
        elif result[1] == "wh":
            chars1 = wenhao  
        
        
    if (len(result) >= 3):    
        if result[2] == "xh":
            chars2 = xinghao       
        elif result[2] == "jh":
            chars2 = jiahao
        elif result[2] == "wh":
            chars2 = wenhao 
        
    
    if (len(result) >= 4):    
        if result[3] == "xh":
            chars3 = xinghao        
        elif result[3] == "jh":
            chars3 = jiahao
        elif result[3] == "wh":
            chars3 = wenhao  
        
    charsList.append(chars)
    charsList.append(chars1)
    charsList.append(chars2)
    charsList.append(chars3)
        
    return charsList
        