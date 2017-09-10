#!/usr/bin/env python
# coding=utf-8



import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.set_cookie("k1","1111")
        print(self.get_cookie("k1"))
        # Set - Cookie: k1 = 1111
        self.render("index.html")


settings = {
    'template_path': 'templates',
    'static_path': 'statics',
    'static_url_prefix': '/statics/',
}

application = tornado.web.Application([
    (r"/index", MainHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()