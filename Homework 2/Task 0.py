# HW2. Task 0
'''Implement a custom list-like container, which stores all input data as strings'''
class StringList:
    def __init__(self, *items): # Transform every single item into a str
        self.data = [str(item) for item in items]
    def __iter__(self): # Make sure that the obj is iterable, so we can use the for loop below.
        return iter(self.data)


my_string_list = StringList(1, 1.0, ["a", "b", "c"])

for el in my_string_list: # Proof that the Items given were converted to strs.
    if type(el) == str:
        print('Nice')

