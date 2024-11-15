import os
from typing import List
import math


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
            continue
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
    """This function returns the occurrence frequency of the target word within the txt file, represented by the chapters list."""
    number_of_chapter_with_target_word = 0
    chapters_list = chapters_chapters_dict(data)
    for chapter in chapters_list:
        if target_word in chapter:
            number_of_chapter_with_target_word += 1

    return round(number_of_chapter_with_target_word/len(chapters_list),2) # round the number so it matches the example output
def term_frequency(target_word: str, chapter_number: int) -> float:
    """The following function outputs the term frequency of the target_word in a specified chapter.
    The function passed test outputs 1 and 2. Function failed test for count_in_chapter('мир', 137) == 0.001."""
    data = read_data(path) # this is a list
    tot_num_words_chapter = 0
    target_word_counter = 0
    chapters_list = chapters_chapters_dict(data) # these will be used for the output formula

    for word in chapters_list[chapter_number]: #check if the target word is the selected chapter
        tot_num_words_chapter +=1
        if word==target_word:
            target_word_counter += 1
    return round(target_word_counter/tot_num_words_chapter,4)
def get_tf_idf(target_word: str, chapter_number: int) -> float:
    """This function provides the  term frequency–inverse document frequency of a target word. It also calculates the idf.
    The function passed all output tests."""
    data = read_data(path)
    chapters_list = chapters_chapters_dict(data)
    tot_chapter_num = len(chapters_list)
    tot_chapter_num_with_target_word = 0

    for chapter in chapters_list:
        if target_word in chapter:
            tot_chapter_num_with_target_word += 1

    idf = math.log(tot_chapter_num/tot_chapter_num_with_target_word)
    tf = term_frequency(target_word,chapter_number)
    return round(tf*idf,3) #this should return tf_idf

script_dir = os.path.dirname(__file__) # откуда запускается скрипт. Таким образом скрипт будет работать и на макос без использования абсолютного пути.
path = os.path.join(script_dir, "war_peace.txt")

data = read_data(path)
target_word = 'python'
chapter_number=3
print(get_tf_idf('дуб', 0))