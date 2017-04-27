# Project Description

Synonym analyzer draws a graph from all synonys in a given language (or specified to a given graph size)

## Structure

The main class ```synonym_graph.py``` reads in a given number of words in a target language and parses thesaurus.com using ```scraper.py```. The graph class takes this data and organizes it in a graph_tools undirected graph and saves to a file in the src/ directory.

## Install

virtualenv dance..
```
cd Synonym_Analyzer
virtualenv env
source env/bin/activate
```

pip tango...
```
pip install -r requirements.txt
```

graph-tools waltz..
(note: this may take some configuring since the graph-tools base-layer is written in c++. Make sure gcc is the appropriate version-- for more info: https://git.skewed.de/count0/graph-tool/wikis/installation-instructions)
```
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install expat
sudo apt-get -y install libsparsehash-dev
sudo apt-get -y install gtk+3
sudo apt-get -y install libboost-all-dev
sudo apt-get -y install graphviz
sudo apt-get -y install build-essential
sudo apt-get -y install libcairo2-dev
sudo apt-get -y install python-pip
sudo apt-get -y install python-dev
sudo apt-get -y install python-matplotlib
sudo apt-get -y install gfortran libopenblas-dev liblapack-dev
sudo apt-get -y install libcgal-dev
sudo apt-get -y install python-numpy
sudo apt-get -y install python2.7-config
sudo apt-get -y install python-cairo
sudo apt-get -y install python-scipy
sudo apt-key adv --keyserver pgp.skewed.de --recv-key 98507F25
echo 'deb http://downloads.skewed.de/apt/trusty trusty universe' | sudo tee -a  /etc/apt/sources.list
echo 'deb-src http://downloads.skewed.de/apt/trusty trusty universe' | sudo tee -a  /etc/apt/sources.list
sudo apt-get update
sudo apt-get -y --force-yes install python-graph-tool
```


### Example

```
python synonym_graph.py
```
Will give you an image 'graph of synonmys in ENGLISH base size-10 span-3.png' of your graph:

![Alt text](src/graph of synonmys in ENGLISH base size-10 span-3.png?raw=true "Graph of a few english synonym clusters of span = 3")


## Authors

* **David Goldstein** 

