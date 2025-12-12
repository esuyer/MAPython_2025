import time
import socket
import sys
from datetime import datetime

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("give me a number between 10 and 20")
time.sleep(1)
num = int(input(""))
if num >= 10 and num <= 20:
  print("thanks!")
else:
  print(IPAddr)
  time.sleep(3)
  sys.exit()
time.sleep(1)
print("now i will need to ask for 2 numbers that are good pairs(sum = 50 OR product = 100)")
time.sleep(1)
num1 = int(input("first number pls: "))
num2 = int(input("second number please: "))
if num1 + num2 == 50 or num1 * num2 == 100:
  print(num1, "and", num2, "arent not good pairs")
else:
  print(num1, "and", num2, "arent not not good pairs")
time.sleep(1)
month = int(input("what month is is (1-12): "))
day = int(input("what day is it(1-31)(note that some dates change so do the date for 2025)"))
if month == 1 and day == 1:
  print(f"its time for yet another new year, being {datetime.now().year}... ")
elif month == 2 and day == 14:
  print("you know how sometime near valentines day, when you are at school and everybody is giving out little gifts to everyone? can i have some?")
elif month == 3 and day == 20:
  print("yooo its my bday!!!")
elif month == 4 and day == 20:
  print("eggs")
elif month == 5 and day == 4:
 print("may the forth be with you")
elif month == 6:
  print("i couldnt find one for june, instead do july 23")
elif month == 7 and day == 4:
  print("")
