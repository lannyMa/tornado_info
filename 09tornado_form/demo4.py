#!/usr/bin/env python
# coding=utf-8

class Fu:
    # def __init__(self):
    #     self.name="maotai..."

    contry="china"
    def show(self):
        print("fu showing")

    def check_valid(self):
        for k,v in self.__dict__.items():
            print(k,v)

f = Fu()
print(f.__dict__.items())  # 仅仅打印对象的属性
##　dict_items([('name', 'maotai...')])