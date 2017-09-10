
## tornado使用cookie实现页面保护
![yanshi.png](http://ww1.sinaimg.cn/large/9e792b8fgy1fjelp2yp7pg20hs0bghdv)

## 实现7天免登录
- 如果不勾选,则cookie寿命为5s,超过5s重定向到login页面
- 如果勾选,  则cookie寿命为7天.
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjemhebr4xg20iz08jn0r)


## set_cookie 中的参数如下：
```
class LoginHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        passowrd = self.get_argument("password", None)
        check = self.get_argument("auto", None)

        if username == "admin" and passowrd == "admin123":
            # 设置cookie寿命为7天
            if check:
                # self.get_secure_cookie()
                self.set_cookie("username", username, expires_days=7)
                self.set_cookie("auth", "1", expires_days=7)
            else:
            # 设置cookie寿命为5s
                r = time.time() + 5
                self.set_cookie("auth", "1", expires=r)
            self.redirect("/manager")
        else:
            self.render("login.html", status_text="登录失败")

    def get(self, *args, **kwargs):
        self.render("login.html", status_text="")
```
- domin：  域名   用于区分域名
- expires：超出时间   单位秒
- path=””  设置权限，有些cookie只能在某些url下生效 如果等于 \，那么默认在全局中生效
- expires_day：设置超出时间 ，单位天

- 如果要设置立即过期：expires=time.time()，即时间设置成当天时间，就是立即过期
```
class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_cookie("auth","1",expires=time.time())
        self.redirect("/login")
```

- 下面就是进入到隐私页面之后，cookie直接立即过期

