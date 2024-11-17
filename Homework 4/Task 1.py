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
    """The following function creates a dictionary from a string. The function sorts the contents of the str,
    transforming the words into their "normal form", and check whether the word is a preposition.The dictionary contains
     the word, the number of times, it appeared in the text and its respective TF. Prepositions are not stored in the dictionary."""

    morph = pymorphy3.MorphAnalyzer()
    frequency_dictionary = {}
    total_num_words = len(contents.split(" "))

    for word in contents.split(' '):
        if str(morph.parse(word)[0].tag) != "PREP": # Test if the iterated word is a preposition, if it is save it in the dictionary
            if word not in frequency_dictionary:
                    normal_form_word = morph.parse(word)[0].normal_form
                    frequency_dictionary[normal_form_word] = [0, 0.0]
            frequency_dictionary[normal_form_word][0] +=1
            if frequency_dictionary[normal_form_word][0] != 0:
                frequency_dictionary[normal_form_word][1] = round(frequency_dictionary[normal_form_word][0]/total_num_words, 3)
    return frequency_dictionary



# Store the contents of txt file in variables and use lowercase method and remove the punctuation.
positive = file_reader('positive').lower().translate(str.maketrans('','',string.punctuation))
negative = file_reader('negative').lower().translate(str.maketrans('','',string.punctuation))

# Remove extra whitespace
positive = ' '.join(positive.split())
negative = ' '.join(negative.split())

# Create a frequency dictionary, contains the number of times a word occurred and its respective tf
positive_dict = frequency_dictionary_creator(positive)
negative_dict = frequency_dictionary_creator(negative)

print(negative_dict)