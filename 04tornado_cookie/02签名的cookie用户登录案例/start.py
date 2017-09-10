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


import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_secure_cookie('username', 'maotai')
        self.set_secure_cookie('password', '123456')
        self.render('login.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        cooike_user = str(self.get_secure_cookie('username'), encoding='utf-8')
        cooike_pass = str(self.get_secure_cookie('password'), encoding='utf-8')
        if username == cooike_user and password == cooike_pass:
            self.write('Hello ' + cooike_user)
        else:
            self.write('用户名或密码错误')


settings = {
    'template_path': 'templates',
}

application = tornado.web.Application([
    (r'/', IndexHandler),
], **settings,
    cookie_secret="508CE6152CB93994628D3E99934B83CC")

if __name__ == '__main__':
    print('http://127.0.0.1:8888')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()