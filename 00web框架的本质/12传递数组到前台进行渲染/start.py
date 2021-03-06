#!/usr/bin/env python
# coding=utf-8
# http://127.0.0.1:8888/index?username=123&password=123456 这样访问
import tornado.ioloop
import tornado.web

INPUT_LIST=[]

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name")
        INPUT_LIST.append(name)
        # self.write("Hello, world")
        self.render("bbs.html",names=INPUT_LIST)

# 配置选项模块
settings = {
    'template_path': 'templates',
    'static_path': 'statics',
    'static_url_prefix': '/sss/',
}


# 路由模块
application = tornado.web.Application([
    (r"/index", MainHandler),],
    ** settings
)


## wsgi模块
if __name__ == "__main__":
    print("http://127.0.0.1:8888/index")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()