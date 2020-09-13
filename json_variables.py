import json

var_json = '{"name":"Charmander", "level":10, "health":75}'
var_dict = {
    "name": "Pikachu",
    "level": 5,
    "health": 50
}

# Turn a JSON string to a dict
load_json = json.loads(var_json)
print(load_json["health"])

# Turn a dict to a JSON string
json_string = json.dumps(var_dict)
print(json_string)

# Format the dumps result
json_string = json.dumps(var_dict, indent=2, separators=(". ", " = "), sort_keys=True)
print(json_string)



