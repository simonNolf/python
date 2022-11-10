import json

def get_data(key, file="config.json"):
    with open(file, "r") as config:
        data = json.load(config)
        return data[key]