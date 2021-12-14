# python -m pip install requests  to install API
# endpoint is public URL that client application use to access the resources
import json
import requests
import xmltodict

api_url = "https://jsonplaceholder.typicode.com/todos/1"

"""GET - retrieve resources"""
response = requests.get(api_url)
print(response.json())
print(response.status_code)  # 200 is accepted
print(response.headers["Content-Type"])

"""POST - Create a new resource"""
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy Milk", "completed": False}
object = json.dumps(todo)
response = requests.post(api_url, object)
print(response.json())
print(response.status_code)  # 201 is create sucessful

"""PUT- Update"""
print("put")
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)

"""PATCH - modify existing resources"""

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
print(response.json())
print(response.status_code)

"""DELETE"""
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json())
print(response.status_code)



# XML to JSON
# pip install xmltodict  # to install the convert between json and xml
import json

# read xml file, use parse method in xmltodict
with open("xml_file.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
# close the XML file
xml_file.close()
# convert xml to json by json dumps method
json_data = json.dumps(data_dict)
# write json data to output file

with open("data.json", "w") as json_file:
    json_file.write(json_data)

#close output file
json_file.close()


# JSON TO XML by etree.ElementTree
# import json module and etree.ElementTree

import json as js
import xml.etree.ElementTree as ET

# read json file by #load method
with open ("quiz.json", "r") as json_file:
    data = js.load(json_file)
# build a root element by #Element method, every XML file must have exactly one root element
root = ET.Element("quiz")
# build sub element of the root by #SubElement method
math = ET.SubElement(root, "maths")
# build a tree of XML by #ElementTree Method
tree = ET.ElementTree(root)
# write the xml file by #write method
tree.write("quiz.xml")




