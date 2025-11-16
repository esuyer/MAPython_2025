money=int(input("Mr.Blob how much money did you get this year"))
if money>70000:
   print("You have to pay",(money-70000)/4, "in taxes")
if money<70000:
   print("you owe no taxes")


print("problem 2")

age=int(input("what is your age"))
if age<3:
   print("you are a baby")
else:
  if age>=3 and age<=9:
    print("you are a kid")
  else:
    if age>=10 and age<=12:
      print("you are a preteen")
    else:
      if age>=13 and age<=17:
        print("you are a teen")
      else:
        if age>18:
          print("you are an adult")
        else:
          if age>65:
            print("you are a senior citizen")