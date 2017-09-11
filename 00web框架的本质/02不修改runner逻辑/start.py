#!/usr/bin/env python
# coding=utf-8

from wsgiref.simple_server import make_server


def new():
    return "new"


def bbs():
    return "bbs"


urls = {
    "/new": new,
    "/bbs": bbs,
}


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ["PATH_INFO"]

    if url in urls.keys():
        func_name = urls[url]
        ret = func_name()
    else:
        ret = "404"
    return ret


if __name__ == '__main__':
    httpd = make_server('', 8003, RunServer)
    print("http://127.0.0.1:8003/new")
    print("http://127.0.0.1:8003/bbs")
    httpd.serve_forever()