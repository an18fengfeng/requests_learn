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
