import os, string, re
from typing import Dict, Union, List
import pymorphy3
import matplotlib.pyplot as plt

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
        if str(morph.parse(word)[0].tag) != "PREP": # Test if the iterated word is a preposition, if it is, save it in the dictionary
            if word not in frequency_dictionary:
                    normal_form_word = morph.parse(word)[0].normal_form
                    frequency_dictionary[normal_form_word] = [0, 0.0]
            frequency_dictionary[normal_form_word][0] +=1
            if frequency_dictionary[normal_form_word][0] != 0:
                frequency_dictionary[normal_form_word][1] = round(frequency_dictionary[normal_form_word][0]/total_num_words, 3)
    return frequency_dictionary
def create_histogram(*dictionaries: Dict):
    """The following function creates a histogram, which shows the TF for each word contained in the dictionary."""
    for dictionary in dictionaries:
        # Extract words and frequencies from the dictionary
        words = list(dictionary.keys())
        frequency = [value[1] for value in dictionary.values()]

        """https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html"""
        plt.figure(figsize=(24, 12))  # Adjust figure size for better readability
        """https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html"""
        plt.bar(words, frequency, color='blue', alpha=0.7)

        # Customize histogram
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.title('Word Frequency in the Review')
        plt.xticks(rotation=90)  # Rotate x-axis labels so that words are readable

        plt.show()
def word_selector(positive_dict: Dict,negative_dict:Dict) -> List[str]:
    """The following function returns a series of lists. The first list contain common words between the dictionaries,
     the second and third lists contain the uniques words between the dictionaries."""
    # initialize output variables
    common_words = []
    positive_unique = []
    negative_unique = []

    # Iterate through the first dictionary and compare each word to the second dictionary to find common words.
    for word,frequency in positive_dict.items():
        if word in negative_dict:
            common_words.append(word) # Save common words
        else:
            positive_unique.append(word) # If word is not in common, it means it unique for the fist dicitonary
    for word in negative_dict.keys():
        if word not in common_words:
            negative_unique.append(word)

    print(f"Общие слова: {common_words}.\n"
          f"Уникальные слова в позитивном отзыве: {positive_unique}.\n"
          f"Уникальные слова в негативном отзыве: {negative_unique}. \n")
    return common_words,positive_unique,negative_unique

# Store the contents of txt file in variables and use lowercase method and remove the punctuation.
positive = file_reader('positive').lower().translate(str.maketrans('','',string.punctuation))
negative = file_reader('negative').lower().translate(str.maketrans('','',string.punctuation))

# Remove extra whitespace
positive = ' '.join(positive.split())
negative = ' '.join(negative.split())

# Create a frequency dictionary, contains the number of times a word occurred and its respective tf
positive_dict = frequency_dictionary_creator(positive)
negative_dict = frequency_dictionary_creator(negative)

# create a pop-up window with a histogram for each dictionary
create_histogram(positive_dict,negative_dict)

# find common and unique words between the dictionaries:
word_selector(positive_dict,negative_dict)