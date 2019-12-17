import json
import time
import datetime

# Playground to generate some dummy json data, keep it here for future reference (too lazy to search on SO again)

# Get utc time
print(time.time())

# convert to utc timestamp
print(datetime.datetime.utcfromtimestamp(time.time()))

# loading dummy data to write in the json file
data = [
    {
        "date": time.time() - 100,
        "message": "a message"
    },
    {
        "date": time.time() - 90,
        "message": "hello"
    },
    {
        "date": time.time() - 80,
        "message": "damnn"
    },
    {
        "date": time.time() - 70,
        "message": ":)"
    },
    {
        "date": time.time() - 10,
        "message": "OK"
    },
    {
        "date": time.time(),
        "message": "RUN FOREST RUNNN"
    },
]

# example writing a json file
with open("./logs.json", "w") as f:
  json.dump(data, f)

# example reading a json file
with open("./logs.json") as f:
  j = json.load(f)
  print(j[0]["date"])
  # Appending data to json file
  j.append({"date": time.time(), "message": "new message"})
  print(j)