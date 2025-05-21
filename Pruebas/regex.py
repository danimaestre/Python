import re

email = "danimAstre@hotmail.com"
regex = r'^[a-zA-z]+@{1}+[a-z]+\.{1}+[a-z]{2,3}$'



validacion = re.match(regex, email)

print("Correo okey \U00002705" if validacion else "Correo incorrecto \U0000274C")

    
   

