#!/usr/bin/env python
# coding=utf-8


import tornado.ioloop
import tornado.web

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
            ## key随便设置
            random_str = self.Handler.get_cookie('uc')

            # 如果前端没这个key,则给初始化以下
            if not self.random_str:
                random_str = self.__genarate_random_str()
                container[random_str] = {}
            # 如果前端有这个key
            else:
                # 判断可以是否在后端有存储, 如果有存,不做处理
                if self.random_str in container.keys():
                    pass
                # 如果不一致 则重新初始化
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


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = Session(self)


class SetHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.session['hello'] = "world"
        self.write('OK')


class GetHandler(BaseHandler):
    def get(self, *args, **kwargs):
        val = self.session['hello']
        self.write(val)


application = tornado.web.Application([
    (r'/set', SetHandler),
    (r'/get', GetHandler),
])

if __name__ == '__main__':
    print('http://127.0.0.1:8888/set')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
