import requests
import json
import jsonpath

data = open("data.json",mode='r')
v_data = data.read()
print(v_data)

print(type(v_data))

json_data = json.loads(v_data) # convert json data to dict

print(type(json_data))

data1 = jsonpath.jsonpath(json_data,'city') #alwys return data in list or array format
data2 = jsonpath.jsonpath(json_data,'school')
data3 = jsonpath.jsonpath(json_data,'students[:1].name')
data4 = jsonpath.jsonpath(json_data,'students[:].name')

print(data1)
print(data2)
print(data3)
print(data4)