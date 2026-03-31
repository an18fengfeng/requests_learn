from wsgiref import headers

import requests
r = requests.get('https://www.baidu.com')
print(r.cookies)
#获取响应的cookie
for key,value in r.cookies.items():
     print(key,value)
#手动携带cookie发送请求
cookie = "BDORZ=27315"
headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
         'Cookie':cookie
     }
r = requests.get("https://www.baidu.com",headers=headers)
#这里看一下请求成功没有
print(r.status_code)
print(r.request.headers)

#session自动管理cookie（不用手动传了）
# 创建会话（关键！自动管cookie）
s = requests.Session()
# 第一次请求：会话自动保存cookie
s.get("https://www.baidu.com")
# 第二次请求：自动带上之前的cookie
w = s.get("https://www.baidu.com")
print(w.text)