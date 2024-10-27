import requests
from bs4 import BeautifulSoup
from typing import List, Union
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
"""Use these requirements to create the final function"""
# Sentence Requirements: =
# a) Every returned sentence shall begin with the keyword.
# b) Every sente length shall be less than max sentece lenght
# b.1) if it is bigger return only the charactes that are within the boundaries
# c) if the personalised URL does not exist, return an empty list


def get_wiki_info(keyword: str, max_num_sentences: int = 10, max_sentence_length: int = 10) -> Union[List[str], None]:
    keyword.replace(" ",'_')
    request_obj = requests.get(f'https://simple.wikipedia.org/wiki/{str(keyword)}')
    soup = BeautifulSoup(request_obj.text, 'html.parser')
    output_list = []
    counter = 0
    for paragraph in soup.find_all('p'): # Find all paragraphs in the html file
        paragraph = str(paragraph.text)
        for sentence in paragraph.split('.'): # Splint the sentences
            sentence = sentence.strip()
            if sentence.startswith(keyword) and counter != max_num_sentences: # check if the sentence starts with <keyword>
                output_list.append(' '.join(sentence.split(' ')[:max_sentence_length])) # append the sentence as a string
                counter += 1 # make sure that we stay within the boundaries of max_num_sentences
    return output_list

keyword = "Neurolinguistic programming"
n=2
m=4
print(get_wiki_info(keyword,max_num_sentences=n,max_sentence_length=m))