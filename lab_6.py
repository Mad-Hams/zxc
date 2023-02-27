import random


#1


data = ["Tom", 22, "Google"]

#1

# tom = tuple(data)
# print(tom)      

#2

# my_tuple = (1, 4, 2, 3, 5)
# print(len(my_tuple))

#3


# name, age, company, position = ("Tom", 37, "Google", "software developer")
# print(name)         # Tom
# print(age)          # 37
# print(position)     # software developer
# print(company)     # Google


#4

# tom = ("Tom", 37, "Google", "software developer")
# print(tom[1:3])     
# print(tom[:3])     
# print(tom[1:])     


#5
# user = ("Tom", 22, "Google")
# name = "Tom"
# if name in user:
#     print("Пользователя зовут Tom")
# else:
#     print("Пользователь имеет другое имя")


#Set
# words = ['hello', 'daddy', 'hello', 'mum']

# wordsSet = set(words);

# print(wordsSet)

# print(len(wordsSet))


# for i in wordsSet:
#     print(i)

# print("daddy" in wordsSet)

# wordsSet.add("sister")
# print(wordsSet)
# wordsSet.discard("sister")
# print(wordsSet)
# wordsSet.remove("hello")
# print(wordsSet)

# months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])  
# months_b = set(["July", "Aug", "Sep", "Oct", "Nov", "Dec"])
 
# all_months = months_a.union(months_b)  
# print(all_months)












# 1


# def fill_tuple(start, end, count):
#     return tuple(random.randint(start, end) for _ in range(count))
# tuple_1 = fill_tuple(0, 5, 10)
# print(f"Tuple 1: {tuple_1}")
# tuple_2 = fill_tuple(-5, 0, 10)
# print(f"Tuple 2: {tuple_2}")
# tuple_3 = tuple_1 + tuple_2
# print(f"Tuple 3: {tuple_3}")
# # Count the number of zeros in the third tuple
# count_zeros = tuple_3.count(0)
# print(f"Количество нулей в tuple_3: {count_zeros}")

        





# 2

# my_tuple = (1, (42, (3.14, ((3+2j), ('Конечная строка', ())))))
# new = my_tuple[1][1][1][1][0]
# print(new)


# 3

# categories = ["Travel", "Lunch", "Dinner", "Entertainment"]
# expenses = [[0 for j in range(len(categories))] for i in range(7)]
# for i in range(7):
#     for j in range(len(categories)):
#         expense = float('{:.2f}'.format(random.random() * 100))
#         expenses[i][j] = expense

# total = 0
# for i in range(7):
#     daily_total = float('{:.2f}'.format(sum(expenses[i])))
#     print("Траты за день", i+1, ":", daily_total)
#     total += daily_total
# print("Фулл трата за неделю:", total)
# print(expenses)


# 4

# student_names = input("Введитее имена: ").split()
# student_tuple = tuple(student_names)
# print("Имена содержащие `ва`:")
# for name in student_tuple:
#     if "ва" in name.lower():
#         print(name)


# 5




# letters = {
#     'а': 'a', 'ә': 'á', 'б': 'b', 'в': 'v', 'г': 'g', 'ғ': 'ǵ', 'д': 'd', 'е': 'e', 'ё': 'io', 'ж': 'j', 'з': 'z',
#     'и': 'i', 'й': 'ı', 'к': 'k', 'қ': 'q', 'л': 'l', 'м': 'm', 'н': 'n', 'ң': 'ń', 'о': 'o', 'ө': 'ó', 'п': 'p',
#     'р': 'r', 'с': 's', 'т': 't', 'у': 'ý', 'ұ': 'u', 'ү': 'ú', 'ф': 'f', 'х': 'h', 'һ': 'h', 'ц': 'ts', 'ч': 'ch',
#     'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'і': 'i', 'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia'
# }

# cyrillic_text = input("Введите казахский текст на кириллице: ")

# latin_text = ''
# for letter in cyrillic_text:
#     latin_text += letters.get(letter.lower(), letter)


# print(latin_text)