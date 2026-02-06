print("Question 1")
print("")
python= ['Java', 'Sratch', 'Python', 'C++']
print(python)
if  'Python' in python:
    index= python.index('Python')
    print("Python is in the list at index", index)
else:
    print("Python is not in the list")
print("")
print("Question 2")
print("")
Grade= ['A', 'C', 'D', 'C', 'B', 'B', 'A', 'A']
print(Grade)
A= Grade.count('A')
print("Got A:", A)
B= Grade.count('B')
print("Got B:", B)
CD= Grade.count('C') + Grade.count('D')
print("Can retake:", CD)
print("")
print("Question 3")
print("")
list= ['Katana', 'great sword', 'spear', 'katana', 'Rapier', 'Cutlass']
print('before adding:',list)
Beginning= list.insert (0, 'Beginning')
print("after adding beginning:", list)
End= list.append('End')
print("after adding end:", list)
list_len = len(list)
if  list_len % 2 == 0:
    middle_index = list_len // 2
    list.insert(middle_index, 'Middle')
    print("after adding middle:", list)
else:
  print(list)
print("")
print("Question 4")
print("")
line= ['Sam', 'Jenna', 'Max', 'Andrew', 'Grace', 'Bob']
print(line)
J_pos= line.index('Jenna')
print('Jenna pos', J_pos+1)
A_pos= line.index('Andrew')
print('Andrew pos', A_pos+1)
infront= line.count('Sam')
print('people in front of Jenna:', infront)
behind= line.count('Grace') + line.count('Bob')
print('people behind Andrew:', behind)
print("")
print("Question 6")
print("")
num_list= [2, 4, 6, 8, 10]
print('before squaring:',num_list)
new_list= []
for i in range  (len(num_list)):
    new_list.append(num_list[i]**2)
print('after squaring:', new_list)
print("")
print("Question 7")
print("")
player= ['Ann', 'Sam', 'Kevin', 'Bob']
replace= player.copy()
replace.remove('Kevin')
replace.insert(2,'Jake')
print('before replacing:', player)
print('after replacing:', replace)
print("")
print("Question 8")
print("")
order= ['Pizza', 'Burger', 'Pasta', 'Fries']
rev_order= []
rev_order= order.copy()
rev_order.reverse()
print('before reversing:', order)
print('after reversing:', rev_order)