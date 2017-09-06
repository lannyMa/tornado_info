#!/usr/bin/env python
# coding=utf-8

# http://blog.csdn.net/iiiiher/article/details/77676487

# cookie很容易被恶意的客户端伪造，加入你想在cookie中保存当前登陆用户的id之类的信息，你需要对cookie做签名以防止伪造，Tornado通过set_secure_cookie和get_secure_cookie方法直接支持了这种功能，要使用这些方法，你需要在创建应用一个密钥，名字为cookie_secret(在settings配置cookie_secret)

# 写cookie过程：
# 将值进行base64加密
# 对除值以外的内容进行签名，哈希算法（无法逆向解析）
# 拼接 签名 + 加密值
# 读cookie过程：

# 读取 签名 + 加密值
# 对签名进行验证
# base64解密，获取值内容
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self,*args, **kwargs):
        if not self.get_secure_cookie("mycookie"):
            # 设置一个加密Cookie所需要的参数
            self.set_secure_cookie("mycookie", "myvalue",expires_days=30, version=None, **kwargs)
            # mycookie | 12: bXl2YWx1ZQ == | 14
            # ca032ad0c63ab61cb159ff478e64e3974cf68637fa9a18991a617268fcd4b5
            self.write("Your cookie was not set yet!")
        else:
            self.write("Your cookie was set!")

settings = {
    'template_path': 'templates',
    'static_path': 'static',
    'static_url_prefix': '/statics/',
}


# 要使用加密的Cookie，你需要在创建应用时提供一个密钥，名字为cookie_secret, 你可以把它作为一个关键词参数传入应用的设置中
application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings,cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")


if __name__ == "__main__":
    print('http://127.0.0.1:8888/')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()