#!/usr/bin/env python
# coding=utf-8



import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.set_cookie("k1","1111")
        print(self.cookies)
        # Set - Cookie: csrftoken = YyiKHO56i34zUATMwZzn22RAXjQogra2wA7Yl7WZPrUydQzQ7GqHU2IAdUR7hUIt
        # Set - Cookie: k1 = 1111
        # Set - Cookie: sessionid = epyrbs62ydk1p915eipukjexdsmqj6wd
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