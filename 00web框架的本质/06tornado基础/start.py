#!/usr/bin/env python
# coding=utf-8
# 使用py3
import tornado.web


# controller 业务逻辑处理
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


# urls 路由系统 路由映射
application = tornado.web.Application([
    (r"/index", MainHandler),
])

# wsgi 服务器
if __name__ == "__main__":
    print("http://127.0.0.1:8888/index")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
