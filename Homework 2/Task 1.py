import os
# HW2. Task 1.1

'''Имплементируйте функцию, которая опишет датасет в папке class_3/hw2/t2_data/flowers(путь будет отличатся:G:\PyCharm Projects\Volgastate_Coding_Course\Homework 2\Files\flowers),
где объекты это изображения, названия папок отвечают атрибуту "type" и в названии каждого изображения содержится информация о цвете цветка *_<color>.jpeg

Json structure example:

{
    "flowers":
    [
        {
            "path": "flowers/daisy/african_daisy_yellow.jpeg",
            "color": "yellow",
            "type": "daisy"
        },
        ...
    ]
}
'''

'''Flower_dic = {'flowers': [{'path': 'lombago.jpg','color':'yellow'},{'path':'lombago2.jpg', 'color':'red'}]} # How it should look like'''
'''flower_dic = {{'path':'', 'type':''}}'''
path_list = []
type_list = []
color_list = []
# Try to open the folders and read the name of the files, and store them.
x = os.listdir('G:/PyCharm Projects/Volgastate_Coding_Course/Homework 2/Files/flowers')
# X is a list of strs. We should use the method listdir while iterating through x.
for flower_type in x:
    type_list.append(flower_type)
    color_list.append(os.listdir(f'G:/PyCharm Projects/Volgastate_Coding_Course/Homework 2/Files/flowers/{flower_type}'))

# print(os.listdir('G:/PyCharm Projects/Volgastate_Coding_Course/Homework 2/Files/flowers/rose'))
print(color_list)