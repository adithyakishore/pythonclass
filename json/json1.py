import json
json_str = '{"subject" : "cybersquare", "grade" : 10}'
python_dict = json.loads(json_str)
print("json string is: ",json_str)
print("python dictionary is :",python_dict)
print(python_dict['subject'])
print(python_dict['grade'])