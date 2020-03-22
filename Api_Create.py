import requests
import jsonpath
import json

url = 'https://reqres.in/api/users?page=2'

# get means read the url data
u_response = requests.get(url)
#text return json data
u_data = u_response.text
print(u_data)

u_statuscode = u_response.status_code # type json data
print(u_statuscode)

u_json_data = json.loads(u_data) # type dict
print(u_json_data)

u_per_page  = jsonpath.jsonpath(u_json_data,'per_page')
print(u_per_page)

u_data_elements = jsonpath.jsonpath(u_json_data,'data')
print(u_data_elements)
print(len(u_data_elements[0]))
#print(len(jsonpath.jsonpath(u_json_data,'data')))

assert u_statuscode == 200