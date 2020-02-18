from random import uniform

R = float(input('Введіть число R: '))
N = int(input('Введіть довжину списка: '))
print()
list = [uniform (0, 100) for i in range (N)]
list.sort()

sum = 1000000
for i in range(len(list)):
    if (R - (list[i] + list[0])) < sum:
        sum = (list[i] + list[0])
        l1, l2 = list[i], list[0]

print(f'Наш список:{list}.')
print(f'Сума 2х елементів: {sum}.')
print(f'Елементи: {l1}, {l2}.')
