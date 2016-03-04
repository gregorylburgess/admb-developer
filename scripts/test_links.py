from bs4 import BeautifulSoup as Soup
import json
import requests
import codecs
import sys 
import urllib
import httplib


visited = list()
bad = list()
base = "https://github.com"


def getlinks(url):
	response = requests.get(base+url)
	soup = Soup(response.text, "html.parser")
	links = soup.select('#readme article a')
	for link in links:
	  addr=link.attrs.get('href')
	  if not(addr in visited):
			 openurl(addr)
	print(visited)


def openurl(url):
	if url[0] == '/':
		print(base+url)
		c = httplib.HTTPConnection(base+url)
		c.request("HEAD", '')
		if c.getresponse().status != 200:
			bad.append(url)
		visited.append(addr)

getlinks("/gregorylburgess/admb-developers/")






