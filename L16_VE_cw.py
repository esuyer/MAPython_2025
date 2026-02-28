#greetings="hello"
#print(greetings)


#num=14

#print("we have " + str(num) + " apples")

#print(f"we have {num} apples")

#print("sam" == "Sam")

#print("cat"<"Cat")

#print("c">"C")

#print("cat" <"apricot")

#word="PYTHON"

#print(word.lower())

#s="banAna"
#print(s.count("a"))
#print(s.count("A"))

#t= s.replace("a","z")
#print(t)

def aA_to_z(s):
  new_str=""
  for i in range (len(s)):
      if s[i] == 'a' or s[i] == 'A':
        new_str+="z"
      else:
        new_str+=s[i]
      
  return new_str

print(aA_to_z("bananA"))



def even_to_dot(g):
  new_st=""
  for i in range (len(g)):
      if i % 2==0:
        new_st+="."
      else:
        new_st+=g[i]
  
  return new_st
print(even_to_dot('python'))




def NoA(s):
  new_str=""
  for i in range (len(s)):
      if s[i] == 'a' or s[i] == 'A':
        new_str+=""
      else:
        new_str+=s[i]

  return new_str

print(NoA("AbrAcadabra"))