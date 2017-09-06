#!/usr/bin/env python
# coding=utf-8


class Fu():
    def check(self,request):
        for k,v in self.__dict__.items():
            print(k,v)

class Zi(Fu):
    def __init__(self):
        self.zname="ziname"

class C():
    def post(self):
        z= Zi()
        z.check(self)

c = C()
c.post()
## zname ziname