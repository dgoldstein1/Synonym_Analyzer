# synonymFetcher.py

# external depent
from urllib import urlopen
import requests
import Queue
from threading import Thread
from bs4 import BeautifulSoup

"""
Created by David on 11/22/2017

English-specific requests for getting synonyms of english words

"""

def scrapeDefinition(word):
	"""parses definition of given word from online
	@params:
	    word 			- Required  : starting point in thesaurus.com (string)
	@return definition (string)
    """    
	url = 'http://www.thesaurus.com/browse/' + word + '?s=t'
	html = urlopen(url).read()
	soup = BeautifulSoup(html,"html.parser")

	#get definition
	definitionBlock = soup.find('div',{"class":"mask"})
	if definitionBlock == None:
		print "Could not find synonym block in parsing for URL: " + url
		return

	definition = ""
	for block in definitionBlock.findAll('strong',{"class":"ttl"}):
		definition += block.renderContents() + ", "

	return definition

def scrapeSynonym(word,key='b08CVJHscZ6rRGfc7MzS',language='en_US', max=5):
	"""
	scrapes synonyms of word from thesaurus.com
	@params:
	    word			- Required  : word to scrape
	    key				- Required  : registed key with http://thesaurus.altervista.org/ (string)
		language		- Optional  : language synonym is in
		max				- Optional  : max n of synonsm (int)

	@return dictionary (word : syn list), or None if no synonyms found or invalid word
	"""
	endpoint = "http://thesaurus.altervista.org/thesaurus/v1"
	url = endpoint + "?word={}&language={}&key={}&output=json".format(word,language,key)
	r = requests.request('GET', url, timeout=5.0)
	if r.status_code == 200:
		try:
			syns = r.json()['response'][0]['list']['synonyms'].split('|')
		except KeyError or TypeError:
			return None

		del syns[max:]
		for i in range(len(syns)):
			syns[i] = syns[i].split(' ')[0] 			

		return {'word' : word,'syns' : syns}
	
