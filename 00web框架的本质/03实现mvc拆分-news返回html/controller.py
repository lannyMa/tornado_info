#!/usr/bin/env python
# coding=utf-8

def new():
    # return "new"
    f = open("./new.html", 'r')
    data = f.read()
    f.close()
    return data


def bbs():
    return "bbs"
