import requests
url="http://baidu.com/"
res=requests.get(url)


#看一下常用的方法
#查看响应内容
print(res.text)
#查看响应状态码
print(res.status_code)
#查看响应对象类型
print(type(res))
#查看响应内容类型
print(type(res.text))
#查看cookies
print(res.cookies)
#响应头
print(res.headers)
