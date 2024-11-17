import os, string, re
from os.path import pathsep
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

# Store the contents of txt file in variables and use lowercase method.
positive = file_reader('positive').lower()
negative = file_reader('negative').lower()

#Remove punctuation
positive, negative = positive,negative.translate(str.maketrans('','',string.punctuation))

# Remove extra whitespace
positive = ' '.join(positive.split())
negative = ' '.join(negative.split())

print(negative)