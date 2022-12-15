import json

user_data = {"name": "John", "age": 30, "city": "New York"}
some_json = json.dumps(user_data, indent= 1)
with open("some_json.json", "w") as file:
    file.write(some_json)

print(some_json)