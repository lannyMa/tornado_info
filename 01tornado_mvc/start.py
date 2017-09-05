#!/usr/bin/env python
# coding=utf-8

## 参考 http://blog.csdn.net/iiiiher/article/details/77461260


import time
import tornado.ioloop
import tornado.web


# 业务逻辑处理模块


# 配置选项模块
from controllers import home


# 静态文件和模板文件的配置
settings = {
    'template_path': 'templates',
    'static_path': 'statics',
}

# 路由模块
## 动态路由系统
application = tornado.web.Application([
    (r"/index/(?P<page>\d*)", home.IndexHandler),
],
    **settings
)

## wsgi模块
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
