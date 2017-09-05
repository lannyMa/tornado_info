#!/usr/bin/env python
# coding=utf-8
import time
import tornado.ioloop
import tornado.web


# 业务逻辑处理模块

class LoginHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        dic = {"status":True,"message":""}
        username = self.get_argument("username")
        password = self.get_argument("password")
        if username=="admin" and password=="admin123":
            pass
        else:
            dic["status"] = False
            dic["message"]="用户名或密码错误"
        import json
        self.write(json.dumps(dic))
    def get(self, *args, **kwargs):
        self.render("login.html")


# 配置选项模块
settings = {
    'template_path': 'template',
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
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
