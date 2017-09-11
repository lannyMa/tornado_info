#!/usr/bin/env python
# coding=utf-8



import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write("index get")
        self.render("index.html")

    def post(self, *args, **kwargs):
        self.write("index post")


settings = {
    'template_path': 'templates',
    'static_path': 'statics',  # 配置了前缀,则显示 /ss/xx.css 如果没配置前缀,则显示 /static/xx.css
    'static_url_prefix': '/sss/'
}

application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)

if __name__ == "__main__":
    print("http://127.0.0.1:8888/index")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
