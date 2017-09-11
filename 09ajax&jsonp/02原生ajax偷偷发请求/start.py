#!/usr/bin/env python
# coding=utf-8



import tornado.ioloop
import tornado.web


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render("login.html")

settings = {
    'template_path': 'templates',
    'static_path': 'statics',
    'static_url_prefix': '/sss/',

}

application = tornado.web.Application([
    (r"/login", LoginHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()