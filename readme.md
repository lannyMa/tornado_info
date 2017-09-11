

## tornado大纲
- 1.cookie
  - 在浏览器段保存的键值对,特性:每次http请求都会携带
  - 实现功能:
    - 用户验证
    - ...
  - cookie设置:
     - tornado,后台设置cookie
       - self.cookies
       - self.get_cookie("k1")
       - self.set_cookie("k1","999")
     - 在浏览器使用js
       - document.cookie
    - 基本cookie
    - 加密的cookie
    - 安全的方式:session

- 2.ajax
  - 伪造的ajax
  - 原生的ajax
  - jquery ajax
  - 跨域ajax请求

- 3.上传文件
  - from表单形式上传
  - ajax
  - jq
  - iframe

- 4.安全
  - xss
  - csrt
    - 限制post请求
- 5.form验证
- 6.验证码



## 参考
存放一些学习tornado时候的阶段性代码

[pyweb框架本质-tornado框架初探](http://blog.csdn.net/iiiiher/article/details/77461260)

[tornado2-通过cookie保护页面](http://blog.csdn.net/iiiiher/article/details/77477606)

[tornado_原生ajax](http://blog.csdn.net/iiiiher/article/details/77488712)

[tornado-jquery ajax](http://blog.csdn.net/iiiiher/article/details/77528964)

[tornado分页实现-从本质到完全实现](http://blog.csdn.net/iiiiher/article/details/77587368)


[tornado诠释cookie](http://blog.csdn.net/iiiiher/article/details/77676487)

[一步一步实现tornado form验证](http://blog.csdn.net/iiiiher/article/details/77689472)
