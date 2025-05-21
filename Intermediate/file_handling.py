###  File handling (Manejo de archivos)  ####

import os

# .txt file

#txt_file = open('my_file.txt', 'r+') #Leer y escribir

txt_file = open('my_file.txt', 'w+')
txt_file.write("Mi nombre es Brais\nMi apellido es Moure\nEdad 35\nMi lenguaje preferido es Python")

# print(txt_file.read()) # Lee todo el fichero
# print(txt_file.read(10))  # Lee solo los primeros 10 caracteres
# print(txt_file.readline()) # Lee linea a linea
# print(txt_file.readline()) # Lee linea a linea
# print(txt_file.readlines()) # Lee como listado (lista)

for line in txt_file.readlines():
    print(line)
    
txt_file.write('\nAunque tambien me gusta kotlin')
print(txt_file.readline())

txt_file.close()
with open ("my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")
    
# os.remove("my_file.txt")


# **************** .json file  ***********************************
# Tiene formato de un diccionario

import json

json_file = open("my_fyle.json", "w+")

json_test = {
    'name': 'Brais',
    'surname': 'Moure',
    'age':35,
    'languages':['Python', 'Swift', 'Kotlin'],
    'website': 'https://moure.dev'
    }

# dump() permite escribir el objeto en el fichero como texto
json.dump(json_test, json_file, indent=3)

json_file.close()

with open ("my_fyle.json") as my_other_file:
    for line in my_other_file:
        print(line)

# Pasamos de un json a un diccionario

json_dict = json.load(open("my_fyle.json"))

print(json_dict)
print(type(json_dict))
print(json_dict['name'])

# .csv file

import csv

csv_file = open("my_fyle.csv", "w+")

csv_write = csv.writer(csv_file)
csv_write.writerow(['name', 'surname', 'age', 'language', 'website'])
csv_write.writerow(['Brais', 'Moure', '35', 'Python', 'https://moure.dev'])

csv_file.close()

with open ("my_fyle.csv") as my_other_file:
    for line in my_other_file:
        print(line)




# .xlsx file
# xml file