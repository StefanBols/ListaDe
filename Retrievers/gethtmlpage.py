#http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup
## CTRL + SHIFT + B 

from bs4 import BeautifulSoup
import requests
import re
import json
import configparser


config = configparser.ConfigParser()
config.read('../config.ini')
configIMDbList = config['DEFAULT']['IMDBLISTS'].split('\n')
imdbLists = list(filter(None, configIMDbList)) # Remove empty lines

url = imdbLists[0]
searchStr = "IMDbReactInitialState.push"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

for script in soup.find_all("script", text=re.compile(searchStr)):
	lines = script.text.splitlines()
	lineWanted = list(filter(lambda x: searchStr in x, lines))[0]
	lineWanted = lineWanted.replace("        ", "")
	lineWanted = lineWanted.replace("IMDbReactInitialState.push(", "")
	lineWanted = lineWanted.replace(");", "")
	jsonObj = json.loads(lineWanted)

	for item in jsonObj["list"]["items"]:
		movieId  = item["const"];
		movie = jsonObj["titles"][movieId]
		print (movie["id"] + ": " + movie["primary"]["title"] + " (" + movie["primary"]["year"][0] + ")")