#!/usr/bin/env python
# coding=utf-8


## 如果传值了,优先使用传递的值,如果未传值,使用默认的
def show(name="maotai"):
    print(name)

show()
show("maming")
# maotai
# maming