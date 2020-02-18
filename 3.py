from random import randint
a =[randint(0,10) for i in range(int(input('n = ')))]
print(a)
summa = 0
for i in a:
    if i == 0:
        summa+=1
print(summa)
