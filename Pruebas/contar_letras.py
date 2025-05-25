string = input("Introduce una palabra o frase: ==> ")

letters = dict.fromkeys(string, 0)

for letter in string:
    letters[letter] += 1
    
print(letters)
