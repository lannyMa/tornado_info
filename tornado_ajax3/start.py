#!/usr/bin/env python
# coding=utf-8

import tornado.web


# 业务逻辑处理模块

class LoginHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):

        username=self.get_argument("username")
        password=self.get_argument("password")
        if username=="admin" and password=="admin123":
            self.render("login.html", right_code="200",error_code="")
        else:
            self.render("login.html", right_code="",error_code="400")

    def get(self, *args, **kwargs):
        self.render("login.html",error_code="",right_code="")

# 配置选项模块
settings = {
    'template_path': 'templates',
    'static_path': 'statics',
}

# 路由模块
application = tornado.web.Application([
    (r"/login", LoginHandler),

],
    **settings
)

## wsgi模块
if __name__ == "__main__":
    print("http://127.0.0.1:8888/login")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
