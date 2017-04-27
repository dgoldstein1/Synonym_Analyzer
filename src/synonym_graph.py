"""
Graph of synonyms of given language
Created by David on 4.19.2017
"""

import sys
import time
import os

from random import randint
import scraper
from graph_tool.all import *

class SynonymGraph:
	"""
	Graphs a network of synonyms based on random words in specified language and specified graph size
	"""
	def __init__(self,size=10,span=3,language='english'):
		"""
		reads In file with all words in language. Creates node for each word and
		creates verticies to corresponding synonyms
		@params:
			size		-optional  : 	# words to scrape and add synonyms
			span 		-optional  : 	# synonyms to parse and add for each word
			language   - optional  : 	language to get words from

		"""
		self._g = Graph(directed=False) 
		self._v_prop = self._g.new_vertex_property("string") #map vertex (int) -> word (string)
		self._verticies = {} #map of word (string) -> vertex (int)
		self._language = language.upper()
		self._size = size
		self._span = span
		self._createGraph()


	def _createGraph(self):
		"""
		reads In file with all words in language. Creates node for each word and
		creates verticies to corresponding synonyms
		@return success
		"""
		try:
			parentDir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
			path = parentDir + "/lib/word_lists/" + self._language + "_Dictionary.txt"
			word_list = open(path,'r').readlines()

		except IOError:
			print "No such file {}".format(path)
			return False

		i = 0
		self._printProgress(i,self._size,'Adding synonyms...')
		while i <= self._size:
			word = word_list[randint(0,len(word_list))]
			word = (word.rstrip('\n')).rstrip('\r').lower() #clean up word

			if self._addNode(word): #successfully added
				self._printProgress(i,self._size,'Added {} Synonyms of {}'.format(self._span,word))			
				i+=1

		return True
			

	def _addNode(self,word):
		"""
		Adds a given word to graph if valid
		@params:	
			 word 		-required		: 	word to add	(string)
		@return  success
		"""

		synonyms = scraper.scrapeSynonyms(word, self._span)
		if synonyms is None: #no synonyms found or invalid word
			return False

		#add vertex for word
		if not self._verticies.get(word):#create only if not already a node
			v = self._g.add_vertex()
			self._verticies[word] = v
			self._v_prop[v] = word

		word_vertex = self._verticies[word] #get vertex id of word

		#add vertex + edge for each synonym
		for synonym in synonyms:


			if not self._verticies.get(synonym):
				v = self._g.add_vertex()
				self._verticies[synonym] = v
				self._v_prop[v] = synonym
			self._g.add_edge(word_vertex, v)

		return True


	def drawGraph(self):
		graph_draw(self._g,vertex_text=self._v_prop,
			output="graph of synonmys in {} base size-{} span-{}.png".format(self._language,self._size,self._span))

	def _printProgress (self,iteration, total, prefix = 'generating tree', suffix = '', decimals = 0, barLength = 40):
	    """
	    Call in a loop to create terminal progress bar
	    @params:
	        iteration   - Required  : current iteration (Int)
	        total       - Required  : total iterations (Int)
	        prefix      - Optional  : prefix string (Str)
	        suffix      - Optional  : suffix string (Str)
	        decimals    - Optional  : positive number of decimals in percent complete (Int)
	        barLength   - Optional  : character length of bar (Int)
	    """
	    formatStr       = "{0:." + str(decimals) + "f}"
	    percents        = formatStr.format(100 * (iteration / float(total)))
	    filledLength    = int(round(barLength * iteration / float(total)))
	    bar             = '#' * filledLength + '-' * (barLength - filledLength)


	    sys.stdout.write('|%s| %s%s %s \r%s ' % ( prefix, bar, percents, '%', suffix)),
	    if iteration == total:
	        sys.stdout.write('\n')
	    sys.stdout.flush()

if __name__ == "__main__":
	start_time = time.time()

	g = SynonymGraph()
	g.drawGraph()

	print("--- executed in %s seconds ---" % (time.time() - start_time))




 
	

 		