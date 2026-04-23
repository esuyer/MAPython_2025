
def is_palendrome(s):  
  n=len(s)
  for i in range(len(s)):
    if s[i] != s[n-1-i]:
      print("Not a palendrome")


  print("It is a palendrome")

    
      
       

print(is_palendrome("racecar"))
      