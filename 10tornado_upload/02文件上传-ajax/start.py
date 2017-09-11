#!/usr/bin/env python
# coding=utf-8

import json
import os

import tornado.web

IMG_LIST = []


class FileUploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("upload.html", img_list=IMG_LIST)

    def post(self, *args, **kwargs):
        ret = {'result': 'OK'}
        print(os.path.dirname(__file__))
        upload_path = os.path.join(os.path.dirname(__file__), 'files')  # 文件的暂存路径
        file_metas = self.request.files["fff"]  # 提取表单中‘name’为‘file’的文件元数据

        if not file_metas:
            print("bad!!!!!!!!!")
            ret['result'] = 'Invalid Args'
            return ret

        for meta in file_metas:
            print("ok!!!!!!!!!!!!!11")
            filename = meta['filename']
            file_path = os.path.join(upload_path, filename)
            print(file_path)
            with open(file_path, 'wb') as up:
                up.write(meta['body'])
                # OR do other thing
            IMG_LIST.append(filename)
        self.write(json.dumps(ret))


settings = {
    'template_path': 'templates',
    'static_path': 'statics',
    'static_url_prefix': '/sss/',
    'cookie_secret': "asfsdfasdf",
    # 'xsrf_cookies': True
}

app = tornado.web.Application([
    (r'/file', FileUploadHandler),
],**settings)

if __name__ == '__main__':
    print("http://127.0.0.1:8080/file")
    app.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
