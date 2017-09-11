#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
from hashlib import sha1
import os, time
import re


# 创建form类
class MainForm(object):
    # 初始化
    def __init__(self):
        self.host = "(.*)"
        self.ip = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"
        self.port = '(\d+)'
        self.phone = '^1[3|4|5|8][0-9]\d{8}$'

    # 验证
    def check_valid(self, request):
        # 循环当前类中的成员，注意此种方法
        for key, regular in self.__dict__.items():
            '''
            通过request.get_argument()来获取用户前端输入的值
            在循环时，不需要关心前端输入值的个数，这里以自定义方法为主
            '''
            post_value = request.get_argument(key)
            # 前端提交的数据与自定义的正则表达式进行匹配验证
            ret = re.match(regular, post_value)
            print(key, ret, post_value)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self, *args, **kwargs):
        obj = MainForm()
        result = obj.check_valid(self)
        self.write('ok')


settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh',
    'login_url': '/login'
}

application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
