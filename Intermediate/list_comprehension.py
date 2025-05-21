### List Comprehension ###

my_original_list = [35, 24, 62, 52, 30, 30, 17,8]

my_list = [i**2 for i in my_original_list ]

print(my_list)

my_list = [i for i in my_original_list if i > 50 ]
print(my_list)

def sum_five (number):
    return number + 5

my_list = [sum_five(i) for i in my_original_list ]
print(my_list)

