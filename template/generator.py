import os
import json
from pathlib import Path

photosList = os.listdir("./photos")
print(photosList)
def getInput(text):
    print(text)
    output = input("> ")

parentDir=Path(__file__).resolve().parent

parentDir=f"{parentDir}".split("/")
parentDir=parentDir[-1]
print(parentDir)
baseJson={
    "hero":"photos/hero.jpg",
    "title":"Whatever the title of this essay is.",
    "fontType":"serif",
    "brand":{
        "logo":"the 2020 daily recap",
        "href":"https://2020.darcylf.me"
    },
    "photos":[]
}

for i in photosList:
    if (i != "hero.jpg"):
        coolDict = {
            "imageURL":f"photos/{i}",
            "caption":"edit me"
        }

        
        baseJson["photos"].append(coolDict)
coolDict = {
    "imageURL":f"photos/hero.jpg",
    "caption":"edit me"
}

        
baseJson["photos"].append(coolDict)

jsonFile = f"{parentDir}.json"
print(jsonFile)

with open(jsonFile, "w") as write_file:
    json_object = json.dumps(baseJson, indent = 4) 
    write_file.write(json_object) 
