'''
Вводиться цілочисельний масив довжини N. Вивести індекси елементів, які менше свого лівого сусіда, та кількість таких чисел.
      (0 ≤ N ≤ 100)
'''
while True:
    while True:
        try:
            n=int(input('Input numbers without space: '))
            break
        except ValueError or TypeError:
            print('Error. Input numbers!')

    n=str(n)
    x=0
    for i in range(len(n)-1):
        if n[i]<n[i+1]:
            x+=1
            print(f'{n[i]}(index {i}) is less than {n[i+1]}')
        elif i==n[-1] or i==n[-2]: break
        else: continue
        print(f'The amount of such numbers is {x}')
    break