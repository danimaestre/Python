### Regular Expressions ###
    # Valen para inspeccionar si una cadena de texto tiene ciertos elementos y nos devuelve las ocurrencias de ese elemento. Hay que importar el modulo re y dentro de este el mas importante es el modulo match() que intentara encontar un patron, enpieza a buscar desde el principio

##################### OPERACIONES ################################

# match() Encuentra solo desde el principio
import re

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I) #re.I ignore case
print(match)
start, end = match.span()
print(my_string[start:end])
print()


match = re.match("Esta no es la lección", my_other_string)
#if not(match == None): # Otra forma
#if match is not None: # Otra forma
if  match != None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string))

# search() Encuentra desde cualquier sitio

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall() Devuelve un array con las ocurrencias

findall = re.findall("lección", my_string, re.I)
print(findall)

# split () devuelve array separando los elementos como le indiquemos (, : \n, etc)

split = re.split(":", my_string)
print(split)
print(re.split(" ", my_string))

# sub() Es para sustituir, solo la 1ª ocurrencia

print(re.sub("[l|L]ección","LECCION", my_string)) # asi cambia ambas con operador |
print(re.sub("Expresiones Regulares","RegEx", my_string))

######## PATRONES PERSONALIZADOS (PATTERNS) ##############

# La 'r' es carater reservado de python para escribir patrones

print("Patrones personalizados (patterns)")
pattern = r"[l|L]ección"
print(re.findall(pattern, my_string))

pattern = r"[l|L]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

# https://regex101.com

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev"
print(re.findall(pattern, email))

direccion = r"^(https?://(www.)?|www.)\w{3,}\.[a-z]{2,3}$"

search = re.search(direccion, "https://www.moure.dev")
print(search)







  
