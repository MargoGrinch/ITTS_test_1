from random import randint
while True:
    n=int(input('n='))
    m=int(input('m='))
    if 0 < m <= 1000 and 0 <= n <= 100:
        break
a=[randint(0,1000) for i in range(n)]
print(a)
max=max(a)
print(max)
for i in range(len(a)):
    if a[i]== max:
        x=a[i-m]
print(x)