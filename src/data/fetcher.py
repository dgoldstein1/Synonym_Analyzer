#fetcher.py

"""
Created by david on 10.24.2016

Fetches language specific synonyms
 a) reads words in
 b) sends multi-threaded requests using ${language}/synonymFetcher.py
"""

# internal dependencies
import sys
import time

# external dependencies
from bs4 import BeautifulSoup
import Queue
from threading import Thread

# language-specific scrapers and parsers
import english.synonymFetcher as english

def getSynonyms(words,language='english', number=5):
	"""
	scrape synonyms of list of words
	@params:
	    words			- Required  : words to scrape
		language		- Optional  : language synonym is in
		max				- Optional  : max n of synonsm (int)

	@return Queue.Queue of finished tasks
	"""
	# get parser by language
	scrapeSynonym = None
	if (language == 'english'):
		scrapeSynonym = english.scrapeSynonym

	if (scrapeSynonym == None):
		print "Language Not Supported " + language
		return Queue.Queue() # return empty queue

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
	que = getSynonyms(words, 'english')
	while not que.empty():
		print que.get()

	print("--- executed in %s seconds ---" % (time.time() - start_time))




 
	

