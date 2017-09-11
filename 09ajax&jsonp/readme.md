- 跨域的ajax

```
$.ajax()
XmlHttpRequest

$.ajax({
    url: '/index',  #跨域请求,浏览器不通过 http://www.csdn.com/xxxx
    })
    
xhr=XmlHttpRequest()
xhr.open("GET","/index")
```
浏览器的限制: ajax发请求的时候,必须同源策略
,只允许给本域发请求


- from验证

- mysql数据库
- pymsql