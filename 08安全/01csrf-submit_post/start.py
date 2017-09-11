#!/usr/bin/env python
# coding=utf-8


import tornado.ioloop
import tornado.web


class CsrfHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("csrf.html")

    def post(self, *args, **kwargs):
        self.write("csrt.post")


settings = {
    'template_path': 'templates',
    'static_path': 'statics',
    'cookie_secret':"asfsdfasdf",
    'xsrf_cookies':True
}

application = tornado.web.Application([
    (r'/csrf', CsrfHandler),
],**settings)

if __name__ == '__main__':
    print('http://127.0.0.1:8888/set')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
