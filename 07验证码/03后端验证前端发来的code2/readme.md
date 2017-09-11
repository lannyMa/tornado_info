

## 实验步骤
- 将原代码跑起来
- 写login.html和indexhandler,前端显示code
- 实现前端code的点击刷新
- 实现后端对code的验证
- 错误则跳转到login
- 错误则提示错误信息

- 前端动态刷新验证码
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjekhegpi8g20cr08jmzt)

- 前端动态刷新验证码-实现原理
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjejxubd3fj20ij0in0ui)

- 用户输入验证码后端验证,如果输入错误提示验证码错误:
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjekn9zefbj20bp09hwew)


- 



 ## 验证码基本原理

- 后端写一个checkcodeImage的handler,前端请求返回图
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjeij3k7qtj20mh0h0tdm)



