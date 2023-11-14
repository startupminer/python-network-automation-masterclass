import json
import pickle


# Description - Serializing to file
# Object - python object
# File - file to serialize object
# Protocol - pickle or json serialization protocol
def serialize(obj: object, file: str, protocol: str):
    if protocol == 'pickle':
        with open(file, 'wb') as f:
            pickle.dump(obj, f)
    if protocol == 'json':
        with open(file, 'w') as f:
            json.dump(obj, f)


# Description - Deserializing data to Python Object
# File - file to serialize object
# Protocol - pickle or json serialization protocol
def deserialize(file: str, protocol: str):
    if protocol == 'pickle':
        with open(file, 'rb') as f:
            formatedObj = pickle.load(f)
            print(formatedObj)
            return formatedObj
    if protocol == 'json':
        with open(file, 'r') as f:
            formatedObj = json.load(f)
            print(formatedObj)
            return formatedObj