import requests

# GET+params只能传简单的字符串
test_params = {
    "name": "afeng",
    "age": 22,           # 我写的是数字
    "is_student": True,  # 我写的是布尔值
    "hobbies": [1, 2, 3] # 我想传个数组
}
#运行后数字，布尔值和数组里面的数字都被转化成字符串的形式了
r = requests.get("http://httpbin.org/get", params=test_params)
print(r.text)

#POST + data（还是只能传简单的字符串，复杂结构照样不行）
test_data = {
    "name": "afeng",
    "hobbies": [1, 2, 3],
    "address": {  # 我想传个嵌套的地址对象
        "city": "长沙",
        "street": "五一路"
    }
}
#运行出来的结果还是简单的字符串
b = requests.post("http://httpbin.org/post", data=test_data)
print(b.text)

#POST + json（什么类型都能传，保持不变）
# 传一个非常复杂的嵌套数据，有数字、布尔、数组、多层对象
test_json = {
    "name": "afeng",
    "age": 22,                     # 数字
    "is_student": True,            # 布尔值
    "hobbies": ["编程", "看电影"], # 数组
    "address": {                   # 嵌套对象
        "city": "长沙",
        "street": "五一路",
        "zip_code": 410000         # 嵌套对象里还有数字
    }
}
#运行出来的和原来的数据类型一样，没有改变
o = requests.post("http://httpbin.org/post", json=test_json)
print(o.text)
res=o.json()
print(res["json"]["hobbies"])
#这里是用json传参的，所以是存在json字段里面的，要引用json，其他几个盒子也是一样的，args和form，都是这样用的