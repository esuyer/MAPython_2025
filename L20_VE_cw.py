
#num = [9, 11, 4, 5] 

#numafter=[]

#if num[0] > num[-1]: 
  
  # for i in range(len(num)):
 #     numafter.append(num[0])
      
#else: 
#    for i in range(len(num)):
#        numafter.append(num[-1])
#print(numafter)


#L1= ["donkey","apples","fly","pears","moose"]
#L2=["moose","donkey","fly"]
#for i in range(len(L1)):
#    if L1[i] in L2:

#L1.remove(L1[i])
#        L1.insert(i,"Banana")


#print(L1)

#alpahbet= #["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#pyramid= int(input("How many rows do you want?"))
#for i in range(pyramid):
#   j=i+1
#   print(alpahbet[i]*j)
   
potion=int(input("How many ounces do you have?"))
vials=0
while potion>0:
   potion=potion - 12
   vials+=1

print("you need ",vials,"vials")
   
   



   