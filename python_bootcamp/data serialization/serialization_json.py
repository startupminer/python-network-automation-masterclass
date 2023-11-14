import json

friends1 = {"Dan": [20, "London", 323443], "Maria": [25, "Madrid", 4352222]}

with open('friends.json', 'w') as f:
    # Use indent arg to format the JSON to be more readable
    json.dump(friends1, f, indent=4)
    # dump s returns a json encoded string
    json_string = json.dumps(friends1, indent=4)
    print(json_string)