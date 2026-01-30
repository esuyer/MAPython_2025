LW= input("Enter a word with both lowercase and upercase letters: ")
for i in range(len(LW)):
    if LW[i]== "a":
      print(LW[i])
    elif LW[i]=="A":
      print(LW[i])


def Chain(X,Y):
    
    if X[0]==Y[-1]:
        print("they are a chain")
    else:
         print("they are not a chain")
         
        
Chain('cat','tac')