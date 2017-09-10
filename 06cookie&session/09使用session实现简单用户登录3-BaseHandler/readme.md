


## 使用session机制实现简易登录系统
- 效果

![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjbcxvrfikg20cr04c0xb)


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