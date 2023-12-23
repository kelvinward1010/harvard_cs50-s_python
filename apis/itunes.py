import json
import requests
import sys

#python itunes.py weezer

if len(sys.argv) != 2:
    sys.exit()
    
url = "https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1]
response = requests.get(url)

data = response.json()

dumpsdata = json.dumps(data, indent=2)

for result in data["results"]:
    print(result["trackName"])