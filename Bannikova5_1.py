import json

def func(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        result = sum(item["score"] * item["weight"] for item in data["data"])
        return round(result, 3)

file_path = "example.json"
print(func(file_path))


