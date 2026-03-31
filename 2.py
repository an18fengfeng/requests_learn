import requests
import json
#添加请求参数
data = {
    'name':'afeng',
    'age':'22'
}#返回来的是 args传入数据的参数，
r = requests.get('http://httpbin.org/get',params=data)
#params是url查询的具体参数
print(r.text)  #发现和r.josn打印出来的一个单引号，一个双引号，
#看一下内容类型    #主要还是text是json格式
print(type(r.text))
#转换内容以字典的形式
print(r.json())
#只有当接口返回的内容是合法的 JSON 格式时，才能调用成功
#dict类型
print(type(r.json()))
#既然能json转字典，那么字典也能转回json
dic = {
    'name':'afeng',
    'age':'22'
}
json_str = json.dumps(dic)   #dumps将字典类型转成json字符串类型
print(json_str)   #json的键值只能是双引号，字典单双都可以
print(type(json_str))  #发现json也是字符串类型

#POST请求
b = requests.post('http://httpbin.org/post',json=data)
#这里的传参参数是data或者json，后面的put，patch也是，通常只有get用params传参
#然后这样做可以不让参数暴露在url里面
print(b.text)#参数全在form表单里面（用data传参的前提下），要不就在json里面（用json传参）


#设置请求头
import requests
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
        'my-test':'Hello World'
}#User-Agent（标准头）     My-Test（自定义头）额外传东西用的
r = requests.get('https://httpbin.org/get', headers=headers)
print(r.text)