#!/usr/bin/env python
# coding=utf-8

#要用py2 来跑

from wsgiref.simple_server import make_server


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ["PATH_INFO"]

    if url == "/new":
        msg = "new"
    elif url == "/bbs":
        msg = "bbs"
    else:
        msg = "404"
    return msg


if __name__ == '__main__':
    httpd = make_server('', 8003, RunServer)
    print("http://127.0.0.1:8003/new")
    print("http://127.0.0.1:8003/bbs")
    httpd.serve_forever()
