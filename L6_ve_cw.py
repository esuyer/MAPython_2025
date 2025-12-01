N=int(input("give me an integer"))
for i in range(0,N+1,1): 
  print(i)
  if i%2==0:
      print("even")
  if i%2==1:
   print("odd")