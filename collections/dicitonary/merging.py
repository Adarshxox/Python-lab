keys = ["name", "place", "postion"]

values = ["john", "bangalore","intern"]   # {"name":"john","place":"bangalore","position":"intern"}

details = {}

for i in range(len(keys)):

    details[keys[i]] = values[i]
      
print(details)