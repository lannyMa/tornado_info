#!/usr/bin/env python
# coding=utf-8


class Fu:
    def __init__(self,name=None,age=None):
        self.name="maotai"
        self.age=22
    def fusing(self):
        print("fu sing")

class Base:
    def baseshow(self,handle):
        for k,v in self.__dict__.items():
            input_value = handle.sing()
            v.fusing()
        print("base show")

class Zi(Base):
    def __init__(self):
        self.f1 = Fu()

z = Zi()
z.baseshow(self)