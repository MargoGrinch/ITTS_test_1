flag = True
while(flag):
 a,b = int(input()), int(input())
 if a >= 0 and b <= 10000:
  flag = False
c = []
for i in range(a,b+1):
  if i % 2 == 0:
   c.append(i)
print(c[::-1])