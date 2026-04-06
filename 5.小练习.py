import requests
class  gain_script:
       def __init__(self):
          self.headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}
          self.url = "https://www.shuzhaige.com/{}/{}.html"#.format("doupocangqiong","102764")
           #首先要请求网站，得到响应，但是每一页链接都在变，所以要处理一下网站链接url
       def get_url_list(self,book_name,start_page=102764,chapter_count=10):
        url_list = []  #先初始一下列表，用来存网站
        for i in  range (chapter_count):
             current_chapter = start_page +i
             #遍历每次循环的章节
             current_url = self.url.format(book_name,current_chapter)
             url_list.append(current_url)
        return url_list
