c = ["java","python","c++","scratch","c#"]
if  "python" in c:
  print("python is in the list")
  print(c.index("python"))
else:
  print("python is not in the list")
Grades = ['A','D','A','B', 'C','A','D','F']
print("# of A's ", Grades.count('A'))
print("# of B'S" ,Grades.count('B'))
print('# of retakes',Grades.count('C') + Grades.count('D') + Grades.count('F'))
L = ['begining','Dog', 'cat','end']
print(L)
L.insert(2,'middle')
print(L)
Line = ['Mike','Bob','Andrew','Joe','Sue','Jenna']
print('Jennas position is',Line.index('Jenna'))
print('Andrews position is',Line.index('Andrew'))
print('Therer are',Line.index('Jenna') - 0,'people ahead of Jenna')
print('Therer are',Line.index('Andrew') - 0,'people ahead of Andrew')
o = [99,33,22]
print(o)
for i in range(len(o)):
   print(o[i]**2)
Names = ['Mike','Bob','Andrew','Joe','Sue','Jenna']
print(Names)
Names[1] = 'Jeff'
print(Names)