flag = True
while(flag):
 n = input("Enter number:\n")
 if(int(n) >= 0) and (int(n) <= 1000000):
  flag = False
sum = 0
for i in range(len(n)):
 sum+=(ord(n[i])-48)
print(sum)