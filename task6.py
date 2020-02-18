a = int(input("input a: "))
b = int(input("input b: "))
sum = 0
index = 0
for i in range(a, b, 1):
    if (i % 3 == 0):
        sum += i
        index += 1
print(int(sum / index))
