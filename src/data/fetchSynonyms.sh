# fetchSynonyms.sh

# Created by David on 11/22/17
# Entry point for fetching and saving synonyms of a given language
# Usage : ./fetchingSynonyms ${language}
# Currently supported languages : 'english'

# check that language is supported

language=$1
if [ ! -d "${language}" ]; then
  echo "No such language supported ${language}"
  exit 1
fi

# run python script to write words to large json
time python fetcher.py ${language}