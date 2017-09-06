#!/usr/bin/env python
# coding=utf-8

from Pagination import Pagination

# 造数据
LIST_INFO = [
    {"username": "maotai", "email": "123456"},
]

for line in range(300):
    tmp = {"username": "maotai", "email": "123456"}
    LIST_INFO.append(tmp)

# 实例化分页程序
page_obj = Pagination(page = 10, LIST_INFO) # page是前端传过来的当前页
current_list = page_obj.current_list_info()  #每页的数据  如每页5条数据
str_page = page_obj.page_str("/index/")     #页码逻辑 /index/1