# Project Description

Synonym analyzer draws a graph from all synonys in a given language (or specified to a given graph size)

## Structure

The main class ```synonym_graph.py``` reads in a given number of words in a target language and parses thesaurus.com using ```scraper.py```. The graph class takes this data and organizes it in a graph_tools undirected graph and saves to a file in the src/ directory.

## Install

#### virtualenv
```
source env/bin/activate
```

#### pip
```
pip install -r requirements.txt
```

#### graph-tools
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

### Run

```
python synonym_graph.py
```
### Example

Graph of a few emotions

![Alt text](https://github.com/dgoldstein1/Synonym_Analyzer/blob/master/src/graphs/graph%20of%20synonmys%20in%20ENGLISH%20base%20size-30%20span-10.png)

Crawling graph of four iterations starting with 'happy'

![Alt text](https://github.com/dgoldstein1/Synonym_Analyzer/blob/master/src/graphs/graph%20of%20synonmys%20in%20ENGLISH%20base%20size-4%20span-3%20-%20crawling%20-%20True.png)


## Authors

* **David Goldstein** - [DavidCharlesGoldstein.com](http://www.davidcharlesgoldstein.com/?github-synonym-analyzer) - [Decipher Technology Studios](http://deciphernow.com/)


