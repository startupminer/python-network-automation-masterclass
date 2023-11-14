import pickle
# dictionary of friends data
friends1 = {"Dan": [20, "London", 323443], "Maria": [25, "Madrid", 4352222]}
friends2 = {"Tony": [20, "New York", 233244], "Jasmine": [29, "China", 223552222 ]}
# Put friends data into a tuple
friends = (friends1, friends2)


# New file open and write in binary mode as pickle is a binary protocol
# Serialize and store data with Pickle
with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)

# Load and deserialize the data from Pickle back into a Python Object.
# Open in read-only mode from binary
with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)
