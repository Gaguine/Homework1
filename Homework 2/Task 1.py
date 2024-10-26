import os
import json

def json_converter(flowers_dic: dict, path : str, file_name = "flower_data.json") -> json:
    """Mark where the json file will be created."""
    json_file_path = f'{path}/{file_name}'
    with open(json_file_path, 'w', encoding="UTF-8") as file:
        json.dump(flowers_dic,  file, sort_keys=False, indent=2, ensure_ascii=False)


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
flowers_dic = {'flowers': []} # initialize essential variables
path = 'G:/PyCharm Projects/Volgastate_Coding_Course/Homework 2/Files/flowers'

type_list = [] # initialize lists to hold types and colors
color_list = []

x = os.listdir(path)
for flower_type in x: # collect flower types and colors
    type_list.append(flower_type)
    color_list.append(os.listdir(f'{path}/{flower_type}'))

for flower_type, files in zip(type_list, color_list):
    for file_name in files:
        # Extract color from the file name using split
        color = file_name


        flower_dic = {'path':f'{path}/{flower_type}/{color}',
                      'color': color,
                      'type': flower_type}

        flowers_dic['flowers'].append(flower_dic)

json_converter(flowers_dic,path)