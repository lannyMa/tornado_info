#!/usr/bin/env python
# coding=utf-8

class Fu():
    def __init__(self):
        self.fname = "fu name"

class Zi(Fu):
    def __init__(self):
        self.zname="zi name"


z = Zi()
print(z.__dict__.items())
## dict_items([('zname', 'zi name')])