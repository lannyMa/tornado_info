#!/usr/bin/env python
# coding=utf-8


import tornado.web
import tornado.ioloop

container = {}


class Session:
    def __init__(self, Handler):
        self.Handler = Handler
        self.random_str = None

    # 随机字符串
    def __genarate_random_str(self):
        import hashlib
        import time
        obj = hashlib.md5()
        obj.update(bytes(str(time.time()), encoding='utf-8'))
        random_str = obj.hexdigest()
        return random_str

    def __setitem__(self, key, value):
        if self.random_str == None:
            random_str = self.Handler.get_cookie('uc')
            if not self.random_str:
                random_str = self.__genarate_random_str()
                container[random_str] = {}

            else:
                if self.random_str in container.keys():
                    pass
                else:
                    random_str = self.__genarate_random_str()
                    container[random_str] = {}
            self.random_str = random_str

        container[self.random_str][key] = value
        # 浏览器写入Cookie
        self.Handler.set_cookie('uc', self.random_str)

    def __getitem__(self, key):
        random_str = self.Handler.get_cookie('uc')
        if not random_str:
            return None
        user_info_dict = container.get(random_str, None)
        if not user_info_dict:
            return None
        value = user_info_dict.get(key, None)
        return value


class BashHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = Session(self)


class SetHandler(BashHandler):
    def get(self, *args, **kwargs):
        self.session['Hello'] = 'World'
        self.write('OK')


class GetHandler(BashHandler):
    def get(self, *args, **kwargs):
        val = self.session['Hello']
        self.write(val)


application = tornado.web.Application([
    (r'/set', SetHandler),
    (r'/get', GetHandler),
])

if __name__ == '__main__':
    print('http://127.0.0.1:8000')
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()