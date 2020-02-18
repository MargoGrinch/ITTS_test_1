'''
Вводиться цілочисельний масив довжини N. Вивести індекси елементів, які менше свого лівого сусіда, та кількість таких чисел.
      (0 ≤ N ≤ 100)
'''
try:
    n=input('Input numbers without space: ')
except ValueError or TypeError: print('Error. Input numbers!')
x=0
for i in range(len(n)-1):
    if n[i]<n[i+1]:
        x+=1
        print(f'{n[i]}(index {i}) is less than {n[i+1]}')
    elif i==n[-1] or i==n[-2]: break
    else: continue
    print(f'The amount of such numbers is {x}')