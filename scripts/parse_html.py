from bs4 import BeautifulSoup
import json
import requests
import codecs
import sys 

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)


def markdown(content):
	url = 'http://heckyesmarkdown.com/go/'
	payload = {'html': content}

	response = requests.post(url, data=payload)
	return response




test=False
with open('html_files.txt') as f:
    html_file = f.readlines()

i=0;
if not test:
	while (i<len(html_file)):
		print(i)
		out=""
		content = open(html_file[i].strip(), 'r').read()
		soup = BeautifulSoup(content, 'html.parser')
		body = str(soup.find(id="content"))
		response = markdown(body)
		outname = html_file[i].strip()[0:-5] + ".md"
	 	outfile = open(outname, 'w')
		outfile.write(response.text.encode("UTF-8"))
		i = i +1
else:
	while (i<1):
		out=""
		content = open(html_file[i].strip(), 'r').read()
		soup = BeautifulSoup(content, 'html.parser')
		body = str(soup.find(id="content"))
		print(str(body))
		response = markdown(body)
		print(response.text)
		i = i +1



