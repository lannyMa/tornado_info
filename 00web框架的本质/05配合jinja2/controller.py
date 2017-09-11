#!/usr/bin/env python
# coding=utf-8
import os

from jinja2 import Template


# pip install jinja2

def bbs():
    f = open(os.path.join("views", "bbs.html"), 'r')
    data = f.read()
    f.close()
    tmp = Template(data)
    data = tmp.render(name="maotai", user_list=['aaron', 'bob', 'cristin', 'danny'])
    return data.encode("utf-8")
