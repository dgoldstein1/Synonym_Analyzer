"""
Graph of synonyms of given language
Created by David on 4.19.2017
"""

import sys
import time
import os

import Queue
from random import randint
import scraper
from graph_tool.all import *

class SynonymGraph:
	"""
	Graphs a network of synonyms based on random words in specified language and specified graph height
	"""
	def __init__(self,height=10,max_span=3,language='english',wordList=None,crawl=None):
		"""
		reads In file with all words in language. Creates node for each word and
		creates verticies to corresponding synonyms
		@params:
			height		-optional  : 	# words to scrape and add synonyms
			span 		-optional  : 	# synonyms to parse and add for each word
			language   	-optional  : 	language to get words from
			wordList 	-Optional  :    read from selected word list
			crawl       -optional  :    crawling graph (String) where height is number of 

		"""
		self._g = Graph(directed=False) 
		self._v_prop = self._g.new_vertex_property("string") #map vertex (int) -> word (string)
		self._verticies = {} #map of word (string) -> vertex (int)
		self._language = language.upper()
		self._height = height
		self._maxSpan = max_span
		self._isCrawlGraph = crawl is not None

		# note that the actual size may vary (some words may not have max_span # synonyms)
		self._maxPossibleSize = 	self._maxSpan ** (self._height + 1) - 1

		if crawl is not None:
			if type(crawl) is not str:
				print "starting word {} is not a string ".format(crawl)
				sys.exit(1)
			self._printProgress(1,1,'created graph');
			self._crawl(crawl)			

		elif not self._createGraphFromList(wordList):
			print "Error initializing graph"
			sys.exit(1)
		
		self._printProgress(self._maxPossibleSize, self._maxPossibleSize, '{:<25}'.format("finished creating graph"))

	def _crawl(self,currWord,iteration=0):
		"""
		crawls graph starting with specified word
		"""
		if iteration==self._height: return #stop condition
		que = scraper.getSynonyms([currWord])
		while not que.empty():
			response = que.get()
			if response is not None:
				self._addNode(response['word'],response['syns'])
				for syn in response['syns']: self._crawl(syn,iteration+1)				


	def _createGraphFromList(self,wordList):
		"""
		reads In file with all words in language. Creates node for each word and
		creates verticies to corresponding synonyms
		@return success
		"""
		self._printProgress(0,1,'Reading word list..')
		try:
			parentDir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
			path = parentDir + "/lib/word_lists/Dictionaries/" + self._language + "_Dictionary.txt"
			if wordList is not None: path = parentDir + "/lib/word_lists/" + wordList
			word_list = open(path,'r').readlines()

		except IOError:
			print "No such file {}".format(path)
			return False
		self._printProgress(1,1,'Reading word list..')

		LOAD = 50 #load 100 words at a time for multithreading
		words_added = 0
		print 'Adding synonyms..'
		while words_added <= self._height:
			words = []
			for word in word_list[words_added:words_added+LOAD]:
				words.append((word.rstrip('\n')).rstrip('\r').lower())

			# for l in range(LOAD):
			# 	word = word_list[randint(0,len(word_list))]
			# 	word = (word.rstrip('\n')).rstrip('\r').lower() #clean up word
			# 	words.append(word)


			que = scraper.getSynonyms(words)
			while not que.empty():
				response = que.get()
				if response is not None:
					words_added+=1
					self._addNode(response['word'],response['syns'])
					if (words_added >= self._height): return True

		return True
			

	def _addNode(self,word,syns):
		"""
		Adds a given word to graph if valid
		@params:	
			word 		-required		: 	word to add	(string)
			syns 		-required 		: 	list of synomys to add
		@return  success
		"""

		#add vertex for word
		self._printProgress(self._g.num_vertices(), self._maxPossibleSize, '{:<10}{:<15}'.format("Adding Word", word))
		if not self._verticies.get(word):#create only if not already a node
			v = self._g.add_vertex()
			self._verticies[word] = v
			self._v_prop[v] = word

		word_vertex = self._verticies[word] #get vertex id of word

		#add vertex + edge for each synonym
		synsAdded = 0
		for synonym in syns:
			if (synsAdded >= self._maxSpan): return True
			if not self._verticies.get(synonym):
				v = self._g.add_vertex()
				self._verticies[synonym] = v
				self._v_prop[v] = synonym
				self._g.add_edge(word_vertex, v)
				synsAdded+=1

		return True


	def drawGraph(self):
		self._printProgress(0,1,"drawing graph")
		graph_draw(
			self._g,
			vertex_text=self._v_prop,
			output_size=(1500,1500),
			output="graphs/graph of synonmys in {} base height-{} span-{} - crawling - {}.png".format(self._language,self._height,self._maxSpan,self._isCrawlGraph))
		self._printProgress(1,1,"finished drawing graph")

	def _printProgress (self,iteration, total, msg, suffix = '', decimals = 0):
	    """
	    Call in a loop to create terminal progress bar
	    @params:
	        iteration   - Required  : current iteration (Int)
	        total       - Required  : total iterations (Int)
	        msg      	- Optional  : msg string (Str)
	        suffix      - Optional  : suffix string (Str)
	        decimals    - Optional  : positive number of decimals in percent complete (Int)
	    """
	    barLength = 80
	    formatStr       = "{0:." + str(decimals) + "f}"
	    percents        = formatStr.format(100 * (iteration / float(total)))
	    filledLength    = int(round(barLength * iteration / float(total)))
	    bar             = '=' * filledLength + '-' * (barLength - filledLength)


	    # sys.stdout.write('[ %s %s%s %s \r%s' % ( msg, bar, percents, '%', suffix))
	    sys.stdout.write('{:<30}[ {:<80} ]{}%  \r'.format(msg,bar,percents))
	    if iteration == total:
	        sys.stdout.write('\n')
	    sys.stdout.flush()

if __name__ == "__main__":
	start_time = time.time()
	#for more word lists : https://github.com/imsky/wordlists
	g = SynonymGraph(height=2,max_span=3,crawl="happy")
	g.drawGraph()

	print("--- executed in %s seconds ---" % (time.time() - start_time))




 
	

 		