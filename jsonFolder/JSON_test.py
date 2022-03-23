import json
from unittest import result

# x =  '{"SSS":"United States of America", "State": "MA", "Country": "United States of America"}'
# inputJSON = json.loads(x)

f = open('addresses.json', encoding="utf-8")
 
# returns JSON object as
# a dictionary
data = json.load(f)

for address in data:
    for key in address:
        if(address[key]==None):
            continue
        else:
            address[key] = str(address[key])

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
f.close()
# Iterating through the json
# list
# search_result = []
# for i in data:
#     isValid = True
#     for key in inputJSON:
#         if(key=='SSS'):
#             continue
#         if(i[key]!=inputJSON[key]):
#             isValid = False
#             break
#     if(isValid):
#         search_result.append(i)

# a = json.dumps(search_result)
# inputJSON2 = json.loads(a)
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(search_result, f, ensure_ascii=False, indent=4)

# for key in inputJSON:
#     print(key)
#     print(inputJSON[key])

# Closing file
# f.close()
