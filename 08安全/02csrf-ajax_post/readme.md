

## csrf原理
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjep4m515pj20jf0jwwgt)


# 通过submit全局刷新跨域请求

## 实现效果
- 没开csrf时,首次访问可以post
- 开了csrf:
  - 首次访问为post时候,提示403禁止
  - 设置: 需要get时html开启```{% raw xsrf_form_html() %} ```,本质生成一个隐藏的input
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjeovfhbnig20ng0b3n0j)

![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjepc78wyzj20js06bmxx)



# 通过ajax点击偷偷跨域请求
- 不携带id
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjeqpdm14hg20sq0m4jyy)

- 携带id

效果:
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjeqmrh7ytg20sq0i0dx1)


参考: http://www.cnblogs.com/wupeiqi/articles/5702910.html

过滤cookie的函数:
```
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
```
过滤出csrf的id
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjepy6ye35j20y108d11o)

