# -*- coding: UTF-8 -*-#
# ------------------------------------
# Name:         rwyaml.py
# Description:
# Author:       wangjx
# Date:         2022/09/23
# ------------------------------------
import yaml
from common.writeLog import writeLog


# 读取配置文件(config.yaml)
def read_yaml(kname):
    try:
        with open('conf/config.yaml') as yfile:
            yobj = yaml.safe_load(yfile)
            return yobj.get(kname)

    except yaml.YAMLError as error:
        writeLog(error)


def write_yaml(kname, kvalue, encoding='utf-8'):
    """在yaml文件写入数据"""
    try:
        with open('conf/config.yaml', encoding=encoding, mode='r') as f:
            doc = yaml.safe_load(f)
            doc[kname] = kvalue
        with open('conf/config.yaml', encoding=encoding, mode='w') as f:
            yaml.safe_dump(doc, stream=f, allow_unicode=True)

    except yaml.YAMLError as error:
        writeLog(error)
