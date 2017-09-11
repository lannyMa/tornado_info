#!/usr/bin/env python
# coding=utf-8

import tornado.web
import uimodule as md
# 业务逻辑处理模块

INPUT_LIST=[]
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        # self.render("bbs.html",names=INPUT_LIST)
        self.render("bbs.html", npm="NPM", names=INPUT_LIST)

    def post(self,*args,**kwargs):
        name = self.get_argument("name")
        INPUT_LIST.append(name)
        self.render("bbs.html", npm="NPM", names=INPUT_LIST)

# 配置选项模块
settings = {
    "template_path":"templates",
    "static_path":"statics",
    "ui_modules": md,
}

# 路由模块
application = tornado.web.Application([
    (r"/index", MainHandler)],
    **settings)

## wsgi模块
if __name__ == "__main__":
    print("http://127.0.0.1:8888/index")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
