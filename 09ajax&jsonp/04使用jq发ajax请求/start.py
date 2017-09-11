#!/usr/bin/env python
# coding=utf-8



import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render("index.html")

    def post(self, *args, **kwargs):
        print(self.get_argument("k1",None))
        self.write('{"status":1,"message":"maotai...."}')


settings = {
    'template_path': 'templates',
    'static_path': 'statics',
    'static_url_prefix': '/sss/',
}

application = tornado.web.Application([
    (r"/index/", IndexHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
