#!/usr/bin/env python
# coding=utf-8



import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("domain2 get")

    def post(self):
        self.write("domain2 post")

settings = {
    'template_path': 'templates',
    'static_path': 'statics',
    'static_url_prefix': '/sss/',
    'cookie_secret': "asfsdfasdf",
    # 'xsrf_cookies': True
}

application = tornado.web.Application([
    (r"/index", MainHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8002)
    tornado.ioloop.IOLoop.instance().start()