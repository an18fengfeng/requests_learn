import requests
from bs4 import BeautifulSoup
class  gain_script:
       def __init__(self,book_name):
          self.book_name = book_name
          self.headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}
          self.url = "https://www.shuzhaige.com/{}/{}.html"#.format("doupocangqiong","102764")
           #首先要请求网站，得到响应，但是每一页链接都在变，所以要处理一下网站链接url
       def get_url_list(self,book_name,start_page,chapter_count):
        url_list = []  #先初始一下列表，用来存网站
        for i in  range (chapter_count):
             current_chapter = start_page +i
             #遍历每次循环的章节
             current_url = self.url.format(book_name,current_chapter)
             url_list.append(current_url)
        return url_list
       def  get_content(self,target_url):
           #这一步是得到内容，肯定要有请求和响应对象
        try :
         response = requests.get(url=target_url,headers=self.headers)
         response.encoding=response.apparent_encoding
         response.raise_for_status()  #处理异常，主要是抛出异常
         soup = BeautifulSoup(response.text, 'html.parser')
         # 新增：先提取大标题（书斋阁的标题在<h1>标签里，直接找h1就行）
         title_tag = soup.find('h1')
         # 如果找到标题，就取出来；没找到就用空字符串
         chapter_title = title_tag.get_text(strip=True) if title_tag else ""
         # 新增：仅3行正文提取（核心，不破坏原有结构）
         soup = BeautifulSoup(response.text, 'html.parser')
         # 先试通用标签，若爬不到就右键检查正文区域改class名（比如read-content/chapter-content）
         content_tag = soup.find('div', id='content')
         # 提取纯文本，没找到就返回提示
         novel_text = content_tag.get_text(strip=True, separator='\n') if content_tag else "未找到小说正文，请检查标签class名！"
         # 把标题和正文拼在一起（中间加两个换行，更美观）
         full_content = f"{chapter_title}\n\n{novel_text}"

         return full_content

        except Exception as e:      #主要是处理异常
            print(f"错误为:{e}")
            return ""
       def save_page(self,novel_content,page_num):
            file_path ="{}第{}页".format(self.book_name,page_num)
            with open(file_path,"w",encoding="utf-8") as f:
                f.write(novel_content)
       def run(self):
           self.book_name = "doupocangqiong"
           url_list = self.get_url_list(self.book_name,102764,2)
           for index,target_url in enumerate(url_list):
            page_num = index+1
            novel_content = self.get_content(target_url)
            if novel_content !="":
                 self.save_page(novel_content,page_num)
if __name__ == "__main__":
    crawler = gain_script(book_name="doupocangqiong")
    crawler.run()