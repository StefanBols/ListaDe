#http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup
## CTRL + SHIFT + B 

from bs4 import BeautifulSoup
import requests
import configparser

config = configparser.ConfigParser()
config.read('../config.ini')
configIMDbList = config['DEFAULT']['IMDBLISTS'].split('\n')
imdbLists = list(filter(None, configIMDbList)) # Remove empty lines

url = imdbLists[0]
print (url)
#r = requests.get(url)

#data = r.text

#soup = BeautifulSoup(data, "html.parser")

#for link in soup.find_all("a"):
#	href = link.get('href')
#	if href and "/title/" in href:
#		print(href)