print ("Problem 1")
colors = ['green', 'blue', 'red', 'orange']
print("The first color is ", colors[0])
print("The last color is ", colors[len(colors)-1])

if "magenta" in colors: 
   print("Found magenta")
else:
   print("Did not find magenta")

for i in range(len(colors)):
   print(i+1, colors[i])

