import random

"""
Упражнение 0

Вам даны списки names и tabs.
Эти списки содержат фамилии сотрудников (names) и их табельные номера (tabs). Напишите программу, которая выведет на
экран список пар имя номер, записанных в один строковый объект через пробел.
"""
def name_tab_creator(names : list, tabs : list):
    name_tab = []
    for name, tab in zip(names,tabs):
        name_tab.append(f"{name} {tab}")
    print(name_tab)

"""
Упражнение 1
На вход дан список digits. Напишите код, который выводит на экран отсортированный по возрастанию список квадратов
 элементов digits.
"""
def num_sort(digits: list):
    new_list = []
    for number in digits:
        number = number**2
        new_list.append(number)
    sorted_digits = sorted(new_list)
    print(sorted_digits)

"""
Упражнение 2
Дан кортеж tpl.
Напишите код, который выведет на экран последний элемент кортежа tpl.

Sample input: tpl = (1, 2, 3, 4)
Sample output: 4
"""
def last_element_tpl(x:tuple):
    print(x[-1])

"""
Упражнение 3
С помощью какой операции можно заменить последний элемент кортежа tpl = (1, 2, 3) на 4?

ОТВЕТ: Пайтон не может менять елементы кортежей также как со списками. Однако. можно полностью 
"переписать" кортеж tpl(новое значение).
tpl = (1,2,3)     # tpl[:-1] + (4,)
tpl = (1,2,4)
print(tpl)

(1, 2, 4)
"""

"""
Упражнение 4
С помощью функции .split() получите список из строки 'hello kitty' и возьмите два последних элемента. В качестве
 ответа введите результат вывода.
 
ОТВЕТ:
x = 'hello kitty'
x_list = x.split()
for word in x_list:
    print(word[-2:])
"""

"""
Упражнение 5
Даны две строки: s1 и s2.
Напишите программу, которая выведет на экран количество уникальных символов, встречающихся в обеих строках.

Sample input: s1 = 'abcdabcd', s2 = 'cdcdef'
Sample output: 2

"""
def unique_letter_counter_using_list(s1 : str, s2 : str):
    phantom_list_1 = []
    phantom_list_2 = []
    letter_count = 0
    for letter in s1:
        if letter not in phantom_list_1:
            phantom_list_1.append(letter)
    for letter in s2:
        if letter not in phantom_list_2:
            phantom_list_2.append(letter)
    for letter1 in phantom_list_1:
        for letter2 in phantom_list_2:
            if letter1 == letter2:
                letter_count += 1
    print(letter_count)
def unique_letter_counter_using_set(s1 : str, s2:str):
    count = 0
    unique_set_1 = set(s1)
    unique_set_2 = set(s2)
    for letter1 in unique_set_1:
        for letter2 in unique_set_2:
            if letter1 == letter2:
                count += 1
    print(count)
def unique_letter_counter_using_set_args(*args : str):
    """ Фунция выводит на экран количество уникальных символов, встречающихся в строках (от двух и блоее) """
    if len(args) < 2:
        print("напишите не менее двух строк.")
    common_letters = set(args[0])
    for arg in args[1:]:
        common_letters = common_letters & set(arg)
    print(len(common_letters))

"""
Упражнение 6*

Прочитайте статью "*args и **kwargs"
https://pavel-karateev.gitbook.io/intermediate-python/sintaksis/args_and_kwargs

Если мы хотим использовать  *args, **kwargs и формальные параметры в функции, какой будет порядок? А если будут
 параметры со значениями по умолчанию?
 ОТВЕТ:
 а) (1. Формальные параметры, 2. *args, 3 **kwargs) 
 b) (1. Формальные параметры, 2. Параметры со значениями по умолчанию. 3.*args, 4. **kwargs)???(я не уверен)

Напишите функцию print_lists. Она принимает набор порядковых аргументов, каждый из которых является списком. Затем
 следует аргумент how (по умолчанию None), в который передаются аргументы с правилами для печати (например,  sep и end).
 Если правила не переданы, следует напечатать списки с sep=' ' и end='\n'.
"""
def print_lists(*args :list, how=None, **kwargs):
    if kwargs == how:
        kwargs['sep'] = '123'
        kwargs['end'] = 'hello'
    for key, value in kwargs.items():
        print(key,value)
    for arg in args:
        for index, element in enumerate(arg):
            if index < len(arg) - 1:
                print(element, end=kwargs['sep'])
            else:
                print(element, end=kwargs['end'])
print_lists([1,2,3], [4,5,6], [7,8,9])






"""
     Task 1. 796. Rotate String
     Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
"""
def str_flipper(s : str, goal : str):
    if len(s) >= 1 and len(goal) <=100: # Provide leetcode constraints
        s_list = []
        goal_list = []
        count = 0
        if s.lower() == goal.lower():   # in case the s word is already identical to goal
            return True

        for s_letter in s.lower():  # create a list for futher comparison
            s_list.append(s_letter)
        for goal_letter in goal.lower():
            goal_list.append(goal_letter)

        while s_list != goal_list:  # using a while loop to compare the lists and change if they are not identical
            s_letter = s_list.pop(0)
            s_list.append(s_letter)
            if s_list == goal_list:
                return True
            count += 1
            if count == len(s_list):    # use a counter to stop the loop. If the counter is equal to the number of letters of the s_list, we should stop the loop.
                return False
    else:
        print("Заданные параметры не подходят.")
        return False

"""
    Task 2. Check If a Word Occurs As a Prefix of Any Word in a Sentence
    Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is 
    a prefix of any word in sentence.
    Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a 
    prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.
    A prefix of a string s is any leading contiguous substring of s
"""
def prefix_checker(sentence: str, searchWord: str):

    if 1 <= len(sentence.lower()) <= 100 and 1 <= len(searchWord.lower()) <= 10:
        sentence_list = []
        check_word = ""
        count = 0
        list_index = []

        for ch in sentence.lower():
            if ch == " ":
                sentence_list.append(check_word)
                check_word = ""
            else:
                check_word += ch

        if check_word:
            sentence_list.append(check_word)
        for i, word in enumerate(sentence_list):
            prefix_in_sentence = (word[0: len(searchWord.lower())])  # compare the first letters(given by the number of letters in check_word) of a word to the check_word.
            if prefix_in_sentence == searchWord.lower():
                list_index.append(i + 1)  # use a list to store the indexes of the words where the prefix occured, return the first item of this list as metioned in the exercise.
                count = + 1
        if count == 0:
            return int(-1) # using count we intinerate how many times the if condition worked(if any prefix was found). If none occured we should output "-1".
        return (list_index[0])

    else:
        print("Заданные параметры не подходят.")

"""
Task 3. Password Generator
['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Напишите генератор паролей. Хороший пароль должен содержать.
* строчные буквы
* заглавные буквы
* цифры
* символы
"""
def password_generator(password_length = 0):
    if password_length == 0: # length not provided when the function was called
        password_length = int(input("Длина вашего пароля: ")) # определяем длину пароля
        password = ""
        while password_length != len(password):
            cap_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            lower_cas_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
            symbol = random.choice("~!@#$%^&*")
            number = random.randrange(10)

            password += cap_letter
            password += lower_cas_letter
            password += symbol
            password += str(number)

        password_list = list(password)
        random.shuffle(password_list)
        password = ""
        for x in password_list:
            password += x
        print(password_length)
        print(password)


