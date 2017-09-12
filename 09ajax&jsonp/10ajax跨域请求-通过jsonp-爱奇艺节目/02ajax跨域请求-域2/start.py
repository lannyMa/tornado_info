#!/usr/bin/env python
# coding=utf-8



import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("domain2 get")
        # self.render("index.html")
        # self.write("alert(123);")
        self.write("func([1,2,3,4])")

    def post(self):
        self.write("domain2 post")


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
    print("http://www.d2.com:8002/index")
    application.listen(8002)
    tornado.ioloop.IOLoop.instance().start()
