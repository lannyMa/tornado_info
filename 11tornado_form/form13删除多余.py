#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

import tornado.web


class IPField:
    REGULAR = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"

    # error_dict 自定义报错信息
    def __init__(self, error_dict=None, required=True):
        self.error_dict = {}

        # 如果自定义了错误信息,更新错误
        if error_dict:
            self.error_dict.update(error_dict)

        # 保存required
        self.required = required

        # 错误信息
        self.error = None
        # 是否匹配
        self.is_valid = None
        # 匹配成功后值是多少
        self.value = None

    # name 字段名(便于提示错误)
    # input_value 用于输入值,用于验证
    def validate(self, name, input_value):
        '''
        :param name: 字段名(便于提示错误)
        :param input_value:
        :return: input_value 用于输入值,用于验证
        '''
        if not self.required:
            # 值允许为空
            self.is_valid = True
            self.value = input_value
        else:
            # 值不允许为空
            if not input_value.strip():
                # 用户输入为空
                if self.error_dict.get("required", None):
                    # 生成错误信息
                    self.error = self.error_dict["required"]
                else:
                    # 提示ip不能为空
                    self.error = "%s is required" % name
            else:
                # 用户输入了ip,接下来判断ip格式
                ret = re.match(IPField.REGULAR, input_value)  # 静态字段IPField.REGULAR
                if ret:
                    # 匹配成功
                    self.is_valid = True
                    self.value = ret.group()
                    # self.value = ret.input_value
                else:
                    # 匹配失败 构造错误信息
                    if self.error_dict.get("valid", None):
                        self.error = self.error_dict["valid"]
                    else:
                        self.error = "%s is invalid" % name


class BaseForm(object):
    def check_valid(self, handle):
        # 循环当前类中的成员，注意此种方法
        flag = True
        value_dict = {}

        # 错误信息
        error_msg_dict = {}
        success_value_dict = {}
        for key, regular in self.__dict__.items():
            # key: ip
            # regular: IPField对象
            # input_value 用户输入的值
            input_value = handle.get_argument(key)

            regular.validate(key, input_value)
            # 如果验证成功
            if regular.is_valid:
                # pass
                success_value_dict[key] = regular.value
            else:
                error_msg_dict[key] = regular.error
                # 如果验证失败
                flag = False
            value_dict[key] = input_value
        return flag, success_value_dict, error_msg_dict


# 创建homeform类
class HomeForm(BaseForm):
    # 初始化
    def __init__(self):
        # self.host = "(.*)"
        # self.ip = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"
        self.ip = IPField(required=True,
                          error_dict={"required": "别闹,不能为空", "valid": "格式错了,兄弟..."})  # required=True 必须要写
        # self.ip = IPField()

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home1.html')

    def post(self, *args, **kwargs):
        obj = HomeForm()
        is_valid, success_dict, error_dict = obj.check_valid(self)
        # self.write('ok')
        # 如果全部验证成功,则打印
        if is_valid:
            print("sucess", success_dict)
        else:
            print("error", error_dict)


settings = {
    'template_path': 'templates',
    'static_path': 'statics',
    'static_url_prefix': '/static/',
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh',
    'login_url': '/login'
}

application = tornado.web.Application([
    (r"/home", HomeHandler),
], **settings)

if __name__ == "__main__":
    print("http://127.0.0.1:8888/index")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
