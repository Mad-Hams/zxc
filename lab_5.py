import random

# letters = list("Hello")
# print(letters)


# students = ['Dimash', 'Syrym', 'Temir']
# print(students[0])
# students[0] = 'Zhan'
# print(students)


# dimash , syrym , temir =  students
# print(dimash)
# print(syrym)
# print(temir)
# # добавляем в конец списка
# students.append("Dinur")
# print(students)
# # добавляем на вторую позицию
# students.insert(1, "Alikhan")  
# print(students)

# students.extend(["Alexsey", "Alpamis"])
# print(students)

# students.pop()
# print(students)

# index = students.index("Zhan")
# print(index)
# students.pop(index)
# print(students)



#1

# students = []
# def sortByClass(e):
#     return e.split()[1]
# for i in range(5):
#     print("Введите имя студента и его предмет ч/з пробел")
#     std = input()
#     students.append(std)
# students.sort(key=sortByClass)
# print('====================')
# print('Сортированный список')
# for i in range(5):
#     print(students[i])



#2

# student_info = [
#     {'name': 'Dimash', 'grades': ['5', '5', '5', '5']},
#     {'name': 'Syrym', 'grades': ['4', '3', '4', '5']},
#     {'name': 'Zhan', 'grades': ['4', '5', '4', '5']},
#     {'name': 'Dinur', 'grades': ['4', '5', '3', '5']},
# ]
# name = input('Введите имя: ')
# for i in range(len(student_info)):
#     if name.lower() == student_info[i]['name'].lower():
#         print('Оценки студента ' + name + ":")
#         print(', '.join(student_info[i]['grades']))
#         break







#3
# user_list = []
 
# while (value := input('Введите число: ')) != '0':
#   try:
#     user_list.append(int(value))
#   except ValueError:
#     ...  
# print(*sorted(user_list), sep='\r\n')

#4
# user_list = []
 
# while (value := input('Введите число: ')) != '0':
#   try:
#     user_list.append(int(value))
#     user_list.sort(reverse=True)
#   except ValueError:
#     ...  

# print(user_list, sep='\r\n')


#5

# random_numbers = set()
# while len(random_numbers) < 6:
#     random_numbers.add(random.randint(1, 49))
# random_numbers = list(random_numbers)
# random_numbers.sort()
# print("Номера для билета:", random_numbers)


#6

def is_sorted(lst):
    if lst == sorted(lst):
        return True
    else:
        return False
 
input_list = []
for i in range(5):
    input_list.append(int(input('Введите число: ')))
print(is_sorted(input_list))