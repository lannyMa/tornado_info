#!/usr/bin/env python
# coding=utf-8

import tornado.web


# 业务逻辑处理模块
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render("bbs.html")

    def post(self):
        self.write("hello post")


# 配置选项模块
settings = {
    "template_path": "templates",  # 模板路径配置
    "static_path":"static",
}

# 路由模块
application = tornado.web.Application([
    (r"/index", MainHandler), ],
    **settings
)

## wsgi模块
if __name__ == "__main__":
    print("http://127.0.0.1:8888/index")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
