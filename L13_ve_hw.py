import random
num=[]
for i in range(5):
  num.append(random.randint(1,10))
  
for i in range(len(num)):
  print(num[i])

print("First + Last:",num[0]+num[4])


for i in range(len(num)):
  if num[i]%2==1:
     print(num[i])


Invites=[input("Enter a name: "),input("Enter a name: "),input("Enter a name: "),input("Enter a name: ")]
print("Invited:",Invites)

N=int(input("Enter a number: "))
Numbers=[]

for i in range(len(Numbers)):
  Numbers.append("+")
  