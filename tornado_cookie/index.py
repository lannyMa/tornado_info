#!/usr/bin/env python
# coding=utf-8
import time
import tornado.ioloop
import tornado.web


# 业务逻辑处理模块
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")


class LoginHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument("username","None")
        passowrd = self.get_argument("password","None")
        check = self.get_argument("auto","None")

        if username == "admin" and passowrd == "admin123":
            if check:
                self.get_secure_cookie()
                self.set_cookie("auth", "1", expires_days=7)
            else:
                r = time.time()+5
                self.set_cookie("auth", "1",expires_days=r)
            self.redirect("/manager")
        else:
            self.render("login.html",status_text="登录失败")

    def get(self, *args, **kwargs):
        self.render("login.html",status_text="")


class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        if self.get_cookie("auth") == "1":
            self.render("manager.html")
        else:
            self.redirect("/login")


class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie("auth", "0")
        self.redirect("/login")


# 配置选项模块
settings = {
    'template_path': 'template',
    'static_path': 'statics',
    'static_url_prefix': '/sss/',
    'cookie_secret':'adfadsfasdfadf',
}

# 路由模块
application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/manager", ManagerHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
],
    **settings
)

## wsgi模块
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
