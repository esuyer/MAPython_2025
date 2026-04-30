import random
import shutil
width = shutil.get_terminal_size().columns
def rollvalues(value, chanceoffail = 5):
  values = []
  for i in range(random.randint(3,6)):
    if random.randint(1,chanceoffail) == chanceoffail:
      values.append(value + random.randint(-3,3))
    else:
       values.append(value)
  return values
for i in range(random.randint(3,6)):
  failed = False
  rval = random.randint(1, 15)
  vals = rollvalues(rval, 5)
  for i in vals:
    if i != rval:
      failed = True
  
  if failed:
    print(f"{str(vals):^{width}} has:\n {'failed':^{width}}")
  else:
    print(f"{str(vals):^{width}} has:\n {'passed':^{width}}")
print("this took me 20 lines of code pleas help this took so long")
