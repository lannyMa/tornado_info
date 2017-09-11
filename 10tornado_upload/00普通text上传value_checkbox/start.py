#!/usr/bin/env python
# coding=utf-8

import tornado.ioloop
import tornado.web
import shutil
import os
import json


class FileUploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("file.html")

    def post(self, *args, **kwargs):
        print(self.get_argument("user"))
        print(self.get_arguments("favor"))

settings = {
    'template_path': 'templates',
    'static_path': 'statics',
    'static_url_prefix': '/sss/',
    'cookie_secret': "asfsdfasdf",
    # 'xsrf_cookies': True
}

app = tornado.web.Application([
    (r'/file', FileUploadHandler),
],**settings)


if __name__ == '__main__':
    print("http://127.0.0.1:8080/file")
    app.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
