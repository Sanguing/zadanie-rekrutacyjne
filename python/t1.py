import json
import os


# data loading
file_path_data = os.path.join(os.path.dirname(__file__), r"..\dane\zbiór_wejściowy.json")
file_path_category = os.path.join(os.path.dirname(__file__), r"..\dane\kategorie.json")

with open(file_path_data, 'r', encoding='utf-8') as file:
    data = json.load(file)
with open(file_path_category, 'r', encoding='utf-8') as file:
    category = json.load(file)

# loading every instance of zbiór_wejściowy.json that is in kategorie.json database then sorting by 'Wartość za uncję (USD)'
sol = []
for data_instance in data: 
    for category_instance in category:
        if data_instance["Typ"] == category_instance["Typ"] and data_instance["Czystość"] == category_instance["Czystość"]:
            sol.append([data_instance, category_instance['Wartość za uncję (USD)']])

'''       
for a in sol:
    print(a)
print('++++++++++')
'''

sol = sorted(sol, key= lambda x:-x[1])

'''
for a in sol:
    print(a)
print('++++++++++')
'''

# displaying top 5
for i in range(5):
    print(sol[i])