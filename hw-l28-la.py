import terminal
words = terminal.inputlist("word")
for i in words:
  if i.__len__() < 5:
    del words[words.index(i)]
print(words)
def alarm(day, onvaca):
  if onvaca == True:
    if 2 <= day <= 6:
      return "get up at 10:00. dont worry, its vacation, you can rest"
    else:
      return "dont wake up... unless you want to go back to 7:00 alarms."
  else:
    if 2 <= day <= 6:
      return "get up at 7:00. there is stuff to do, ok?"
    else:
      return "get up at 10:00, you can sleep a bit longer, its the weekend"
print(alarm(int(input("what day is it? (1-sun,2-mon,3-tue...) ")), input("is it vacation rn? (yes=True, no=False)")=="True"))
