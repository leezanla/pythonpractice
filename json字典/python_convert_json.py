import json
data = '[{"name": "小红", "age": 24, "gender": "male"}, {"name": "小明", "age": 23, "gender": "male"}]'
data = json.loads(data)
for i in data:
    if i.get("name") == "小明":
        print(i)










