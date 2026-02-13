#fruit = ['apple', 'banana', 'cherry', 'apple', 'apple']
#if  "apple" in fruit:
#print("Yes, 'apple' is in the fruits list")

#if "blueberry" in fruit:
#  ind = fruit.index('blueberry')
  #print("fruit is at index", ind)
#else:
 # print("fruit not in list")

#count = fruit.count('apple')

#print(count)

#fruit.append('blueberry')
#fruit.append('mango')

#print("before ", fruit)
#fruit.insert(0, 'tomato')
#print("after ", fruit)

#fruit.remove('tomato')
#print("after remove ", fruit)

#fruit.pop()
#print("after pop ", fruit)

#f = fruit.pop(1)
#print("after pop(1) ", fruit)
#print("popped item ", f)

#fruit.clear()
#print("after clear ", fruit)


#Coding = ['Java', 'Python', 'C++', 'JavaScript', 'C#', 'PHP', 'Swift', 'Go', 'Rust', 'Kotlin']

#if  "Python" in Coding:
#  print("Python is at index", Coding.index("Python"))
#else:
#   print("Python is not in the list")



#Grades=['A','B','C','D','C','B','A','D','C','D']
#print("I got", Grades.count('A'),"A's")
#print("I got", Grades.count('B'),"B's")
#print("Can retake:",Grades.count('D')+Grades.count('C'))

RanList=['Rug','Sofa','Table','Chair','Bed','Lamp','Rug','Carpet']
print("before:", RanList)
RanList.insert(0,'Beginning')
RanList.insert(9,'End')
print("after:", RanList)
if len(RanList)%2==0:
   RanList.insert(len(RanList)//2,'Middle')
  
