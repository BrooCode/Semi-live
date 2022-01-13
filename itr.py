import json

intent = {"intents":[]}
with open('test.json', 'r+') as f:
    json.dump(intent, f, indent=4)

with open('response.json', 'r+') as f:
    data = json.load(f)
    with open('test.json', 'r+') as t:
        temp = json.load(t)
        for i in range(len(data)):
            s = "what is " + data[i]['tag']
            dic={"tag":data[i]['tag'],"patterns":[s],"responses":[data[i]['answer']],"context": [""]}
            temp["intents"].append(dic)
        json.dump(temp, t, indent=4)     
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()

