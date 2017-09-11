#!/usr/bin/env python
# coding=utf-8
import tornado.web

LIST_INFO = [
    {"username": "maotai", "email": "123456"},
]
for line in range(300):
    tmp = {"username": "maotai", "email": "123456"}
    LIST_INFO.append(tmp)


class Pagination:
    def __init__(self, current_page, all_item):
        all_pager, c = divmod(len(all_item), 5)
        if c > 0:
            all_pager += 1
        try:
            current_page = int(current_page)
        except:
            current_page = 1
        if current_page <= 0:
            current_page = 1

        self.current_page = current_page
        self.all_pager = all_pager
        self.all_item=all_item

    @property
    def start(self):
        return (self.current_page - 1) * 5

    @property
    def end(self):
        return self.current_page * 5

    def current_list_info(self):
        current_list = LIST_INFO[self.start:self.end]
        return current_list

    def page_str(self, baseurl):
        list_page = []

        # 上一页
        if self.current_page > 1:
            last_page = '<a href="%s%s">上一页</a>' % (baseurl, self.current_page - 1)
        else:
            last_page = '<a href="%s%s">上一页</a>' % (baseurl, self.current_page)
        list_page.append(last_page)

        # 页码页
        if self.all_pager < 11:
            s = 1
            t = 11
        else:
            if self.current_page <= 6:
                s = 1
                t = 11
            elif self.current_page > 6:
                if self.current_page + 5 > self.all_pager:
                    s = self.all_pager - 11
                    t = self.all_pager
                else:
                    s = self.current_page - 5
                    t = self.current_page + 5

        for p in range(s, t + 1):

            if p == self.current_page:
                tmp = '<a class="active" href="%s%s">%s</a>' % (baseurl, p, p)
            else:
                tmp = '<a href="%s%s">%s</a>' % (baseurl, p, p)
            list_page.append(tmp)

        # if self.current_page>1:
        #     syyp = self.current_page - 1
        # else:
        #     syyp = self.current_page
        #
        # if self.current_page > len(self.all_item):
        #     xyyp = len(self.all_item)
        # else:
        #     xyyp = self.current_page
        #
        # syy = '<a href="%s%s">上一页</a>' % (baseurl, syyp)
        # xyy = '<a href="%s%s">下一页</a>' % (baseurl, xyyp)
        # list_page.insert(0,syy)
        # list_page.append(xyy)



        # 下一页
        if self.current_page< self.all_pager:
            next_page = '<a href="%s%s">下一页</a>' % (baseurl, self.current_page+1)
        else:
            next_page = '<a href="%s%s">下一页</a>' % (baseurl, self.current_page)
        list_page.append(next_page)

        # 跳转到
        jump = """<input type="text" /><a onclick="Jump('%s',this);">GO</a>"""%(baseurl,)
        script="""<script>
            function Jump(baseUrl,ths){
                var val = ths.previousElementSibling.value;
                if(val.trim().length>0){
                    location.href = baseUrl+val;
                }
            }
            </script>
        """
        list_page.append(jump)
        list_page.append(script)
        return "".join(list_page)


class IndexHandler(tornado.web.RequestHandler):
    # def get(self, *args, **kwargs):
    def get(self, page):
        page_obj = Pagination(page, LIST_INFO)
        current_list = page_obj.current_list_info()
        str_page = page_obj.page_str("/index/")
        self.render("home/index.html", list_info=current_list, current_page=page, str_page=str_page)

    def post(self, page):
        username = self.get_argument("username", "")
        email = self.get_argument("email", "")

        tmp = {"username": username, "email": email}
        LIST_INFO.append(tmp)
        self.redirect("/index/" + page)
