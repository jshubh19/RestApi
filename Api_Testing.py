#Api testing in python using requests library
#techsckool.com


import requests
import json
import jsonpath

v_data = requests.get("http://www.techsckool.com/")
print("-------------ResponseData-------------")
print(v_data)

print("------------Type--------------------")
print(type(v_data))

print("-------------HttpStatus---------------")
print(v_data.status_code)

print("---------------Header---------------")
print(v_data.headers)

print("---------------URL------------------")
print(v_data.url)

print("----------------Cookies---------------")
print(v_data.cookies)

print("---------------EncodingVersion----------")
print(v_data.encoding)

print("-------------TextData-------------------")
#print(v_data.text)