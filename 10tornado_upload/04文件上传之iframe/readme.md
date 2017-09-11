



![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjexsyxkx4j20qg0f9gu3)


参考:
http://www.cnblogs.com/wupeiqi/articles/5703697.html
http://www.cnblogs.com/wupeiqi/articles/5702910.html

## 表单上传文件

默认form的enctype是第一个,即平时发post,form会隐含自带第一个.
```html
{#<form action='file'  method='post' enctype="application/x-www-form-urlencoded">#}
<form action='file' enctype="multipart/form-data" method='post'>
```


## iframe页面不刷新
兼容性更好...所有浏览器都支持iframe
