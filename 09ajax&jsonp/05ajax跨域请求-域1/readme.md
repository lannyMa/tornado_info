


## 两个域都可以正常访问-通过ip
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjff8egyzug20iv0giaqb.gif)

## 两个域都可以正常访问-通过域名
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjff8engp7g20iv0gitpn.gif)

## 不允许跨域请求
![](http://ww1.sinaimg.cn/large/9e792b8fgy1fjff8e7et7g20iv0gi49p.gif)
```
<input type="button" value="ajax" onclick="DoAjax();">

<script type="text/javascript" src="/sss/jquery-1.12.4.min.js"></script>
<script>
    function DoAjax() {
        $.ajax({
{#            url: '/index',#}
{#            url: 'http://www.d1.com:8001/index',#}
            url: 'http://www.d2.com:8002/index',
            type: "POST",
            data: {"k1": "v1"},
            success: function (arg) {
                console.log(arg);
            }
        })
    }
</script>
```