import os, string, re
from os.path import pathsep
from typing import Dict, Union, List
from uu import decode
import pymorphy3, matplotlib

def file_reader(file_name: str) -> str:
    """The following function reads the contents of a txt file located in the reviews folder and return them as a str. The contents may be assigned to a variable."""
    script_dir = os.path.dirname(__file__)
    path = f"{script_dir}/reviews/{file_name}.txt"
    text = ""
    with open(path, 'r', encoding='utf-8') as file:
        for phrase in file:
            text += phrase
    return text
def frequency_dictionary_creator(contents: str) -> Dict:
    """The following function creates a dictionary from a string. The dictionary contains the word, the number of times it appeared in the text."""
    frequency_dictionary = {}
    total_num_words = len(contents.split(" "))
    for word in contents.split(' '):
        if word not in frequency_dictionary:
            frequency_dictionary[word] = [0, 0.0]
        frequency_dictionary[word][0] +=1
        if frequency_dictionary[word][0] != 0:
            frequency_dictionary[word][1] = round(frequency_dictionary[word][0]/total_num_words, 3)
    return frequency_dictionary



# Store the contents of txt file in variables and use lowercase method.
positive = file_reader('positive').lower()
negative = file_reader('negative').lower()

#Remove punctuation
positive = positive.translate(str.maketrans('','',string.punctuation))
negative = negative.translate(str.maketrans('','',string.punctuation))

# Remove extra whitespace
positive = ' '.join(positive.split())
negative = ' '.join(negative.split())

# Create a frequency dictionary, contains the number of times a word occurred and its respective tf
positive_dict = frequency_dictionary_creator(positive)
negative_dict = frequency_dictionary_creator(negative)

print(negative_dict)