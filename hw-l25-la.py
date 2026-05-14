phrase = input("give me a phrase: ").lower()
letterfreq = {}
for i in phrase:
  if i in letterfreq:
    letterfreq[i] += 1
  else:
    letterfreq[i] = 1
letterfreq = dict(sorted(letterfreq.items()))
print(("2"+str(letterfreq)+"1").replace("2{", "{\n").replace("}1", "\n}").replace(", ", "\n").replace(": 1\n", ": 1 *\n").replace(": 2\n", ": 2 **\n").replace(": 3\n", ": 3 ***\n").replace(": 4\n", ": 4 ****\n").replace(": 5\n", ": 5 *****\n").replace(": 6\n", ": 6 ******\n").replace(": 7\n", ": 7 *******\n").replace(": 8\n", ": 8 ********\n").replace(": 9\n", ": 9 *********\n").replace(": 10\n", ": 10 **********\n").replace("\\\\", "\\"))
