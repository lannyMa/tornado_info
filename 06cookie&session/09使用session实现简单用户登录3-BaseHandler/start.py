#!/usr/bin/env python
# coding=utf-8


import tornado.web

container = {}


class Session:
    def __init__(self, Handler):
        self.Handler = Handler

    # 随机字符串
    def __genarate_random_str(self):
        import hashlib
        import time
        obj = hashlib.md5()
        obj.update(bytes(str(time.time()), encoding='utf-8'))
        random_str = obj.hexdigest()
        return random_str

    def set_value(self, key, value):
        random_str = self.__genarate_random_str()
        container[random_str] = {}
        container[random_str][key] = value
        self.Handler.set_cookie("u", random_str)
        random_str = self.Handler.get_cookie('uc')

    def get_value(self, key):
        random_str = self.Handler.get_cookie("u")
        user_info_dict = container[random_str]
        value = user_info_dict[key]
        return value


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session=Session(self)

class IndexHandler(BaseHandler):
    def get(self):
        if self.get_argument("u", None) in ["maotai", "admin"]:
            s.set_value("is_login", True)
            s.set_value("name",self.get_argument("u",None))
            print(container)
        else:
            self.write("请登录")


class ManagerHandler(BaseHandler):
    def get(self):
        val = s.get_value("is_login")
        if val:
            self.write(s.get_value("name"))
        else:
            self.write("失败")


settings = {
    'template_path': 'templates',
    'static_path': 'static',
    'static_url_prefix': '/statics/',
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/manager", ManagerHandler),
], **settings)

if __name__ == "__main__":
    print('http://127.0.0.1:8888/')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
