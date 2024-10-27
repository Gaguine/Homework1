import requests
from bs4 import BeautifulSoup
"""
Implement a function which will retrieve information from https://simple.wikipedia.org.
It shall request information from https://simple.wikipedia.org/wiki/<keyword> and return a list of sentences. Every returned sentence
shall begin with <keyword>. ???

Every sentence length shall be less than <max_sentence_length>. If there is more than <max_num_sentences> sentences, which start with <keyword>,
then return only <max_num_sentences> first sentences. If sentence contains more <max_sentence_length> words, then strip the rest of this sentence.

If https://simple.wikipedia.org/wiki/<keyword> doesn't exists, then return an empty list.


from typing import List, Union

def get_wiki_info(keyword: str, max_num_sentences: int = 10, max_sentence_length: int = 10) -> Union[List[str], None]:
    url = "https://simple.wikipedia.org/wiki/" + keyword
    pass
"""
# Use a variable to store the keyword
# Use an f string to create the custom URL

# Sentence Requirements:
# a) Every returned sentence shall begin with the keyword.
# b) Every sente length shall be less than max sentece lenght
# b.1) if it is bigger return only the charactes that are within the boundaries
# c) if the personalised URL does not exist, return an empty list

keyword = 'Python'
r = requests.get(f'https://simple.wikipedia.org/wiki/{keyword}') # Create a response object
print(r.text) # this prints the response of the server?? and the html file I will later need. What Encoding should I use???
print(type(r.text))