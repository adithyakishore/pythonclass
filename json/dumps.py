import json
python_dict ={"department": "physics", "hod" : "thomas"}
json_str = json.dumps(python_dict)

print("json string is: ",json_str)
print("python dictionary is :",python_dict)