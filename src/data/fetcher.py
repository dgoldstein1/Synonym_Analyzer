#fetcher.py

"""
Created by david on 10.24.2016

Fetches language specific synonyms
 a) reads words in
 b) sends multi-threaded requests using ${language}/synonymFetcher.py
"""

# internal dependencies
import sys
import argparse
import os

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

def readInWords(language):
	"""
	reads a .txt file into a list of string where each line is an index
	@param 		language	string 	-Required : language to read in words from 
	@return		word list   array             : list of words w/o any carriage returns	
	"""
	try:
		path = os.path.abspath(os.path.join(os.getcwd())) + '/lib/word_lists/dictionaries/{}_Dictionary.txt'.format(language.upper())
		rawWordList = open(path,'r').readlines()

	except IOError:
		print("No such file {}".format(path))
		return []

	# remove '\r' and '\n' chars
	cleanedWordList = []
	for word in rawWordList:
		cleanedWordList.append((word.rstrip('\n')).rstrip('\r').lower())
	return cleanedWordList


if __name__ == "__main__":

	# parse args
	parser = argparse.ArgumentParser(description='Fetches language specific synonyms.')
	parser.add_argument('language', type=str ,help='The language to get synonyms of')
	args = parser.parse_args()

	# read in dictionart
	words = readInWords(args.language)

	# fetch synonyms:
	que = getSynonyms(words, args.language)
	while not que.empty():
		word = que.get()
		if (word is not None and word != 'None'):
			print ','

