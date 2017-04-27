"""
Created by david on 10.24.2016
"""

import sys
import time
import random
from bs4 import BeautifulSoup
from urllib import urlopen

reload(sys)
sys.setdefaultencoding('utf-8')


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

def scrapeSynonyms(word,number):
	"""
	scrapes synonyms of word from thesaurus.com
	@params:
	    word 			- Required  : starting point in thesaurus.com (string)
	    number 		    - Required  : number of synonyms to scrape (int)

	@return synonyms (string[]), or None if no synonyms found
	"""
	url = 'http://www.thesaurus.com/browse/' + word + '?s=t'
	html = urlopen(url).read()
	soup = BeautifulSoup(html,"html.parser")


	try:
		#check if there are results
		validBlock = soup.find('div',{"class":"mask"})
		for b in validBlock.findAll('li'):
			if  b.get('id') == 'words-gallery-no-results':
				return None
		#get synonym list
		synblock = soup.find('div',{"class":"relevancy-list"}) #synonym box
		i = 0
		synonyms = []
		for syn in synblock.findAll('a'):
			if i >= number:
				break
			word = syn.span.renderContents()
			synonyms.append(word)				
			i = i + 1
	except:
		return None


	if len(synonyms)==0:
		return None
	return synonyms




if __name__ == "__main__":
	start_time = time.time()

	#examples 
	
	synonyms = scrapeSynonyms("test", 5)
	print synonyms

	definition = scrapeDefinition('test')
	print definition 

	print("--- executed in %s seconds ---" % (time.time() - start_time))




 
	

