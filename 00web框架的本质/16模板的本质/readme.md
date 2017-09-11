
## 模板引擎的实质
整个过程其实就是将一个html转换成一个函数，并为该函数提供全局变量，然后执行该函数！！ 

![](http://ww1.sinaimg.cn/large/9e792b8fgy1fhnrybjctdj20vv0ar13d)
test.py
```
#!/usr/bin/env python
# coding=utf-8

namespace= {"name":"maotai","data":[11,22,33]}
code = '''def hellocode():return "name %s,age %d"%(name,data[0])'''

func = compile(code,'<string>',"exec")

exec(func,namespace)

result=namespace['hellocode']()
print (result)
```

简言之理解:

通过namespace执行函数,而在执行函数前,函数所使用的全局变量已经定义了.
```
namespace= {"name":"maotai","data":[11,22,33],'hellocode':def hellocode():return "name %s,age %d"%(name,data[0])}
```