import json

# Deserialize and load the JSON object
with open('friends.json', 'r') as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)

# Triple quotes to multiline string format
json_string = """{
    "Dan": [
        20,
        "London",
        323443
    ],
    "Maria": [
        25,
        "Madrid",
        4352222
    ]
}"""

# load s for deserializing a string object
strObj = json.loads(json_string)
print(type(strObj))
print(strObj)