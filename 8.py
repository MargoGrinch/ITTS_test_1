n = int(input('Введіть довжину масиву: '))
massive = list(map(int, input().split()))
max_num = max(massive)
max_num_index = 0

for i in reversed(massive):
    if i == max_num:
        max_num_index = massive.index(i)
        break
massive = massive[max_num_index + 1:]

print(f'Кількість елементів після {max_num}: {len(massive)}')
