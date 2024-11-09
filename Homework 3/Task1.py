import json
import os
from numpy.ma.core import count
from typing import List

def read_data(path) -> List[str] :
    data = open(path, 'r', encoding='utf-8').read()
    return data.split('\n')
def word_dictionary(data:list) -> dict:
    '''
    Напишите программу, которая переберет все слова и занесет их в словарь (назвать его можете как угодно).
    Увеличивайте счётчик при добавлении каждого нового слова, чтобы посчитать сколько раз это слово встречается в тексте.
    '''
    word_dic = {}
    for word in data:
        if word not in word_dic:
            word_dic[word] = 1
        if word in word_dic:
            word_dic[word] += 1
    return word_dic
def chapters_chapters_dict(data:list)->List[List[str]]:
    """The following function creates a list of lists, where the objects in the array are the separated chapters of the txt file war_peace."""
    chapter = []
    chapters_list = []
    for word in data:
        if "new chapter" not in word:
            chapter.append(word)
        else:
            chapters_list.append(chapter)
            chapter=[]
    return chapters_list
def chapter_frequency(target_word: str, data: List[str]) -> float:
    """This functin returns the occurance frequency of the target word within the txt file, represented by the chapters list."""
    number_of_chapter_with_target_word = 0
    chapters_list = chapters_chapters_dict(data)
    for chapter in chapters_list:
        if target_word in chapter: number_of_chapter_with_target_word += 1

    return number_of_chapter_with_target_word / len(chapters_list)

path = 'G:\PyCharm Projects\Homework1\Homework 3\war_peace.txt'
data = read_data(path)
target_word = 'война'
print(chapter_frequency(target_word,data))