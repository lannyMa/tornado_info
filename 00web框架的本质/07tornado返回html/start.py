#!/usr/bin/env python
# coding=utf-8

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("bbs.html")


application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    print("http://127.0.0.1:8888/index")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
