# d = {
#     "name":"Dimash", 
#     "age": 22, 
#     "course": 3
# }
# print("Student name",  d["name"])
# print("Student age",  d["age"])
# print("Student course",  d["course"])

# # x = d.get("name")
# # print(x)
# d["favoriteProgaLang"] = "PHP"
# print(d)

# del d["favoriteProgaLang"]
# print(d)

# d.pop("age")
# print(d)

# dCopy = d.copy();
# print(dCopy)

# print(len(dCopy))

# for k, v in dCopy.items(): 
#     print(k, v)


# names = ("Dimash", "Aidos", "Erkin")
# age = 20
# showInfo = dict.fromkeys(names, age)
# print(showInfo)
# print(showInfo["Dimash"])









# Задача 2.1
# n = int(input())
# river_country = {}
# rivers = []
# river = ""
# country = ""
# for i in range (0, n, 1):
#     river = input()
#     country = input()
#     river_country.update({river:country})
#     rivers.append(river)
# for i in range (0, n, 1):
#     print(rivers[i] + " находится в  " + river_country.get(rivers[i]))
# river = input()
# if(river_country.get(river) == None):
#     print("Нет такой реки в словаре.")
# else:
#     print("В словаре есть такая река.")

# print("")

# Задача 2.2
# comm_d = {}
# comm_input = ""
# comm_name = ""
# comm_text = ""
# while(True):
#     comm_input = input()
#     if(comm_input == ""):
#         break
#     var = 0
#     for i in comm_input:
#         if (i == ":"):
#             var = 1
#         if(var == 0):
#             comm_name += i
#         else:
#             if(i != ":"):
#                 comm_text += i
#     print(comm_name)
#     print(comm_text)
#     comm_d.update({comm_name:comm_text})
#     comm_name = ""
#     comm_text = ""
# print(comm_d)
# print(len(comm_d))

# print("")

# # Задача 2.3
# phone_d = {}
# phone_input = ""
# phone_number = ""
# phone_name = ""
# k = int(input())
# for i in range (0, k, 1):
#     phone_input = input()
#     var = 0
#     for i in phone_input:
#         if (i == " "):
#             var = 1
#         if(var == 0):
#             phone_number += i
#         else:
#             if(i != " "):
#                 phone_name += i
#     phone_d.update({phone_name:phone_number})
#     phone_number = ""
#     phone_name = ""
# req = input()
# if(phone_d.get(req) == None):
#     print("В словаре нет такого названия.")
# else:
#     print(phone_d.get(req))

# print("")

# # Задача 2.4
worker_d = {}
worker_input = ""
worker_name = ""
worker_num = ""
worker_month = ""
z = int(input())
for i in range (0, z, 1):
    worker_input = input()
    var = 0
    for i in worker_input:
        if (i == " "):
            var += 1
        if(var == 0):
            worker_name += i
        if(var == 1):
            if(i != " "):
                worker_num += i
        if(var == 2):
            if(i != " "):
                worker_month += i
    worker_d.update({worker_name:worker_month})
    worker_name = ""
    worker_num = ""
    worker_month = ""
print(worker_d)

monthreq = input()

for key in worker_d:
    if(monthreq == worker_d.get(key)):
        print(key)


