#!/usr/bin/env python
# coding=utf-8

class Fu():
    def __init__(self):
        self.fname = "fu name"

    def check(self):
        for k,v in self.__dict__.items():
            print(k,v)

class Zi(Fu):
    def __init__(self):
        self.zname="zi name"


z = Zi()
z.check()
## zname zi name