"""
Created by david on 10.24.2016
"""

import sys
import time
import random
from bs4 import BeautifulSoup
from urllib import urlopen
from gevent.pool import Pool
import requests
import Queue
from threading import Thread

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
	
def getSynonyms(words,language='en_US', number=5):
	"""
	scrape synonyms of list of words
	@params:
	    words			- Required  : words to scrape
		language		- Optional  : language synonym is in
		max				- Optional  : max n of synonsm (int)

	@return Queue.Queue of finished tasks
	"""
	#TODO: pass args to scrapeSynonym
	que = Queue.Queue()
	threads_list = list()
	for word in words:
		t = Thread(target=lambda q, arg1: q.put(scrapeSynonym(arg1)), args=(que, word))
		t.start()
		threads_list.append(t)

	for t in threads_list:
		t.join()

	return que


if __name__ == "__main__":
	start_time = time.time()

	#example usage:
	words = ['beautiful', 'sweet', 'pretty', 'gorgeous', 'lovely', 'handsome', 'good', 'better', 'best', 'bad', 'worse', 'worst', 'wonderful', 'splendid', 'mediocre', 'awful', 'fantastic', 'ugly', 'clean', 'dirty', 'wasteful', 'difficult', 'comfortable', 'uncomfortable', 'valuable', 'worthy', 'worthless', 'useful', 'useless', 'important', 'evil', 'angelic', 'rare', 'scarce', 'poor', 'rich', 'disgusting', 'amazing', 'surprising', 'loathesome', 'unusual', 'usual', 'pointless', 'pertinent']
	que = getSynonyms(words)
	while not que.empty():
		print que.get()

	print("--- executed in %s seconds ---" % (time.time() - start_time))




 
	

