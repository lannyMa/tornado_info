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

container={}
class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args, **kwargs):
        # 判断用户名字
        if self.get_argument("u",None) in ["maotai","admin"]:
            import hashlib
            import time
            # 随机字符串(根据时间) 作为 key
            obj = hashlib.md5()
            obj.update(bytes(str(time.time()),encoding='utf-8'))
            random_str = obj.hexdigest()
            container[random_str]={}
            container[random_str]["k1"]=123
            container[random_str]["k2"]=self.get_argument("u",None)+"parentes"
            container[random_str]["is_login"]=True
            self.set_cookie("iiiiii",random_str)
        else:
            self.write("请登录")


class ManagerHandler(tornado.web.RequestHandler):
    def get(self):
        random_str = self.get_cookie("iiiiii")
        current_user_info=container.get(random_str,None)
        # 如果用户没发过来这个cookie
        if not current_user_info:
            self.redirect("/index")
        else:
        # 如果用户发过来了这个cookie
            # 如果cookie is_login为真  ----判断防止伪造
            if current_user_info.get("is_login",None):
                temp = "%s - %s"%(current_user_info.get("k1",""),current_user_info.get("k2",""))
                self.write(temp)
            else:
                self.redirect('/index')
settings = {
    'template_path': 'templates',
    'static_path': 'static',
    'static_url_prefix': '/statics/',
}

# 要使用加密的Cookie，你需要在创建应用时提供一个密钥，名字为cookie_secret, 你可以把它作为一个关键词参数传入应用的设置中
application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/manager", ManagerHandler),
], **settings)


if __name__ == "__main__":
    print('http://127.0.0.1:8888/')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()