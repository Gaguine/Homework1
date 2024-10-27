import os
import json
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
def json_converter(flowers_dic: dict, path : str, file_name = "flower_data.json") -> json:
    """Mark where the json file will be created."""
    json_file_path = f'{path}/{file_name}'
    with open(json_file_path, 'w', encoding="UTF-8") as file:
        json.dump(flowers_dic,  file, sort_keys=False, indent=2, ensure_ascii=False)
def dataset_fetcher(path:str) -> dict:
    """creates a dictionary using the provided path"""
    flowers_dic = {'flowers': []}  # initialize output variable
    rel_path = path.replace('G:/PyCharm Projects/Volgastate_Coding_Course/','')

    type_list = []  # initialize lists to hold types and colors
    color_list = []
    x = os.listdir(path)

    for flower_type in x:  # collect flower types and colors
        type_list.append(flower_type)
        color_list.append(os.listdir(f'{path}/{flower_type}'))

    for flower_type, files in zip(type_list, color_list):
        for file_name in files:
            # Extract color from the file name using replace and strip
            color = file_name.replace('.jpeg','').replace(flower_type,'').replace("flowers",'').replace("flower",'').replace('_'," ").replace('justanother','').strip()
            # Create blueprint
            flower_dic = {'path': f'{rel_path}/{flower_type}/{file_name}',
                          'color': color,
                          'type': flower_type}
            # Store blueprints
            flowers_dic['flowers'].append(flower_dic)

    return flowers_dic


path = 'G:/PyCharm Projects/Volgastate_Coding_Course/Homework 2/Files/flowers'
flowers_dic = dataset_fetcher(path)
json_converter(flowers_dic,path)
# HW2. Task 1.2
class FlowersDataset:
    def __init__(self,json_file_path: str): # provide the object with a dataset property
      with open(json_file_path, "r", encoding='utf-8') as file:
          self.data = json.load(file) # read through the json file and store the data as a dictonary.
    def get_items(self, properties: dict) -> [list[str], str]:
        output_list=[]
        for flower in self.data['flowers']:
            for key,value in properties.items():
                if properties[key] == flower[key] or properties[key] in flower[key]:
                    output_list.append(flower['path'])
        return output_list


# json_file_path = f'{path}/flower_data.json'
# flowers_database = FlowersDataset(json_file_path)
# properties = {"color": "red"}
# print(flowers_database.get_items(properties))


