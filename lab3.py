#1----------------------------
a=2
b=6
for x in range(b-a+1):
    print(x+a)
#2----------------------------
from random import randint

a=randint(1, 10)
b=randint(1, 10)
if a<b:
    for x in range(b-a+1):
        print(x+a)
else:
    for x in range(a-b+1):
        print(x+b)
#3-----------------------------
a=8
b=3

for x in range(a-b+1):
    if (x+b)%2!=0:
        print(x+b)

