#!/usr/bin/env python
# coding=utf-8



import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render("index.html")

    def post(self, *args, **kwargs):
        self.write("domain1 post")


settings = {
    'template_path': 'templates',
    'static_path': 'statics',
    'static_url_prefix': '/sss/',
    'cookie_secret': "asfsdfasdf",
    # 'xsrf_cookies': True
}

application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)

if __name__ == "__main__":
    print("http://127.0.0.1:8001/index")
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()
