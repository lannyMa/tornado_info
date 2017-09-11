#!/usr/bin/env python
# coding=utf-8
import os
import time


def new():
    # return "new"
    f = open(os.path.join("views", "new.html"), 'r')
    data = f.read()
    f.close()
    return data


def bbs():
    f=open(os.path.join("views","bbs.html"),'r') ## 这里是路径的jion
    data = f.read()
    f.close()
    data=data.replace("{{item}}", str(time.time()))
    return data
