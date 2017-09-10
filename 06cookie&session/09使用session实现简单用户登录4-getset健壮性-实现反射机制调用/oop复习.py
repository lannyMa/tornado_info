#!/usr/bin/env python
# coding=utf-8

class DictDemo:
    def __init__(self, key, value):
        self.dict = {}
        self.dict[key] = value

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __len__(self):
        return len(self.dict)


dictDemo = DictDemo('key0', 'value0')  # 自动执行 __setitem__
print(dictDemo['key0'])  # value0       # 自动执行 __getitem__
dictDemo['key1'] = 'value1'
print(dictDemo['key1'])  # value1
print(len(dictDemo))  # 2


# 上面的对象就相当于自己创建了一个内建类型相似的字典，当实例中有类似字典的操作的时候
dictDemo1 = {"key0":"value0"}
print(dictDemo1["key0"]) #value0