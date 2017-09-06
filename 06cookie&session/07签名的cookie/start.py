#!/usr/bin/env python
# coding=utf-8

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self,*args, **kwargs):
        if not self.get_secure_cookie("mycookie"):
            # 设置一个加密Cookie所需要的参数
            self.set_secure_cookie("mycookie", "myvalue",expires_days=30, version=None, **kwargs)
            # mycookie | 12: bXl2YWx1ZQ == | 14
            # ca032ad0c63ab61cb159ff478e64e3974cf68637fa9a18991a617268fcd4b5
            self.write("Your cookie was not set yet!")
        else:
            self.write("Your cookie was set!")

settings = {
    'template_path': 'templates',
    'static_path': 'static',
    'static_url_prefix': '/statics/',
}


# 要使用加密的Cookie，你需要在创建应用时提供一个密钥，名字为cookie_secret, 你可以把它作为一个关键词参数传入应用的设置中
application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings,cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")


if __name__ == "__main__":
    print('http://127.0.0.1:8888/')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()