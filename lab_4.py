#1
#1.1
# str = "Hello world"
# print(len(str))

#1.2
# num = 50
# str_1 = str(50)
# print(type(str_1))

#1.3

# str = "Hello world"

# if 'world' in str:
#     print("Существует")
# else:
#     print("Нет")

#1.4
# list = ['Я', 'изучаю', 'Python']
# stroka = ' '.join(list)
# print(stroka)

#1.5
# code = ord("a")
# print(code)

#1.6

# name = "Tom"
# surname = "Smith"
# fullname = name + " " + surname
# print(fullname) 


#1.7
# str1 = "Dimash"
# str2 = "dimash"
# print(str1 == str2)
 
# print(str1.lower() == str2.lower())  

#1.8
# str1 = "Dimash"
# str2 = "dimash"
# print(str1 == str2)
 
# print(str1.upper() == str2.upper())  

#1.9
# string = "hello world"
 
# # с 0 до 5 индекса
# sub_string1 = string[:5]
# print(sub_string1)      
 

# sub_string2 = string[2:5]
# print(sub_string2)      
 

# sub_string3 = string[2:9:2]
# print(sub_string3)      # lowr


#1.10
# stroka = 'mall'
# stroka = 'b' + stroka[1:]
# print(stroka)


#2

# studentList = []

# while True:
#     print("+ - Добавить.\nl - Вывести Список.\ns - Вывести отсортированный спиисок.\ne - Выйти с программы")
#     cmd = input()
#     if cmd == "+":
#         print("ФИО")
#         fio = input()
#         studentList.append(fio)
#         print("Группа")
#         group = input()
#         studentList.append(group)
#     elif cmd == "l":
#         print("Список студентов")
#         for student in studentList:
#             print(student)
#     elif cmd == "s":
#         sortedList = studentList
#         sortedList.sort()
#         print("Список студентов")
#         for student in sortedList:
#             print(student)
#     elif cmd == "e":
#         break

#3

# string = str(input("Введите слово: "))
# upper = 0
# lower = 0
# for i in string:
#     if i.isupper():
#         upper += 1
#     else:
#         lower += 1
# if upper > lower:
#     print(string.upper())
# else:
#     print(string.lower())



# a = input()
# b = input()
# while not(a.isdigit() and b.isdigit()):
#     a, b = input(), input()
# print(int(a) + int(b))


# data = 5

# while not (data == 0) :
#    print(data)
#    data = data - 1

