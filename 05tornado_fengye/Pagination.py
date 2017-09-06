#!/usr/bin/env python
# coding=utf-8

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
        current_list = self.all_item[self.start:self.end]
        return current_list

    def page_str(self, baseurl):
        list_page = []
        # 上一页  页码  下一页 必须按照顺序添加到list_page
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
