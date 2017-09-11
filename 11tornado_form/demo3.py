#!/usr/bin/env python
# coding=utf-8

class Fu:
    def fushow(self, request):
        print(request.name)  ## 访问C类字段
        request.cshow()      ## 调用C类方法

class Zi(Fu):
    pass

class C:
    def __init__(self):
        self.name = "maotai..."

    def cshow(self):
        print("c showing...")

    def post(self):
        z = Zi()
        z.fushow(self)

c = C()
c.post()
