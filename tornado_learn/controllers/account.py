#!/usr/bin/env python
# coding=utf-8
import tornado.web


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
