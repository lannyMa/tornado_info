## 获取cookie和设置cookie代码逻辑
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjeiys8i3nj213v0gsju9)


## session概述
参考:

http://www.cnblogs.com/xinsiwei18/p/5836381.html

http://www.cnblogs.com/maociping/p/5351340.html

https://blog.ansheng.me/article/python-full-stack-way-tornado-cookie-and-session.html

在Tornado中是不提供像Cookie这种直接设置Session的，需要我们自己写插件来进行对Session的增删改

Session的数据是保存在服务端的，如果要应用Session必须要依赖Cookie，因为Cookie的值就等于Session的Key

Session在内存中的存储方式如下:
- session key的数据结构
```

{
    "第一个人-随机字符串xxxxxx":{
        "k1":"v1",
        "k2":"v2",
    }
    "第二个人-随机字符串yyyyy":{
        "k1":"v1",
        "k2":"v2",
    }
}
```

- 随机字符串设置cookie
```
self.set_cookie("iiiii",random_str)
```

![](http://ww1.sinaimg.cn/large/9e792b8fgy1fja87en7gcj20q80cn0t1)




