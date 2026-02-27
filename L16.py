"""
Problem 1. All a’s to z
Write a function with 1 parameter: a string S. This function should create and return a copy of S
where all a’s (both uppercase and lowercase) are changed to z.
Do not use function replace. Write an algorithm like the one we learned.
Example:
aA_to_z(&#39;abrAkADaBRa&#39;)  &#39;zbrzkzDzBRz&#39;
"""
print ("Problem 1")
def aA_to_z(S):
   new_str = ""
   for i in range(len(S)):
      if S[i] == 'a' or S[i] == 'A':
         new_str += 'z'
      else:
         new_str += S[i]
   return new_str

print(aA_to_z("banana"))

"""
Problem 2. Even to dots
Write a function with 1 parameter: a string S . This function should create and return a copy of S
where all letters on even positions are changed to dots (&#39;.&#39; character).
Examples:
even_to_dot(&#39;Python&#39;)  &#39;.y.h.n&#39;
even_to_dot(&#39;HOP&#39;)  &#39;.O.&#39;
"""
print ("Problem 2")
def even_to_dot(S):
   new_str = ""
   for i in range(len(S)):
      if i % 2 == 0:
         new_str += '.'
      else:
         new_str += S[i]

   return new_str

print(even_to_dot("Python"))


"""
Problem 3. Remove all a’s
Write a function with 1 parameter: a string S. This function should create and return a copy of S
where all a’s (both uppercase and lowercase) are absent.
Do not use function replace. Write an algorithm like the one we learned.
Examples:
remove_aA(&#39;abrAkADaBRa&#39;)  &#39;brkDBR&#39;
remove_aA(&#39;baNanA&#39;)  &#39;bNn&#39;
Tip: if stuck, start with your solution from problem 1 and think how you could modify it to create a
string without a’s.
"""
print ("Problem 3")
def remove_aA(S):
   new_str = ""
   for i in range(len(S)):
      if S[i] != 'a' and S[i] != 'A':
         new_str += S[i]

   return new_str
  

print(remove_aA("banana"))


"""
Problem 4. Upper lower
Write a function with 1 parameter: a string S. This function should create and return a copy of S
where all characters on even positions are uppercased, and all characters of odd positions are
lowercased.
Example:
upper_lower(&#39;OUtstAnDINg&#39;)  &#39;OuTsTaNdInG&#39;
Tip: functions lower/upper will be useful for transforming the letters.
"""
print ("Problem 4")
def upper_lower(S):
   new_str = ""
   for i in range(len(S)):
      if i % 2 == 0:
         new_str += S[i].upper()
         #new_str += chr(ord(S[i]) - 32)
      else:
         new_str += S[i].lower()
         #new_str += chr(ord(S[i]) + 32)
   
   return new_str
  

print(upper_lower("OUtstAnDINg"))


"""
Problem 5. Before letter m
Write a function with 1 parameter: a string S made of lowercase letters. It should create and return a
copy of S where all letters that come before letter “m” in the alphabet are removed.
Examples:
before_m(&#39;scramble&#39;)  &#39;srm&#39;
before_m(&#39;computer&#39;)  &#39;omputr&#39;
Tip: remember that you can compare the letters using &lt;, &gt;, &lt;=, &gt;=.
Problem 6. Important position
Write a function with 2 parameters: a string S and an integer N. It should create and return a copy of
S where the characters at position N is uppercased, and the rest are lowercased. (You can assume
that N is a valid position for S.)
Examples:
up_at_pos(&#39;PYthOn&#39;, 2) &#39;pyThon&#39;
up_at_pos(&#39;wOo&#39;, 0) &#39;Woo&#39;
Tip: with slicing you can solve this problem without loops.
"""
print ("Problem 5")
def before_m(S):
   new_str = ""
   for i in range(len(S)):
      if S[i] >= 'm':
         new_str += S[i]
         #new_str += chr(ord(S[i]) - 32)

   return new_str


print(before_m("scramble"))


"""
Problem 7. Multiply a string
Write a function with 2 parameters: a string S and an integer N. It should create and return a string
made of N repetitions of S.
You are not allowed to use * operator to multiply a string by an integer for this problem.
Examples:
mul_str(&#39;a&#39;, 5) &#39;aaaaa&#39;
mul_str(&#39;beep&#39;, 3) &#39;beepbeepbeep&#39;
"""
print ("Problem 7")
def mul_str(S, N):
   new_str = ""
   for i in range(N):
      new_str += S

   return new_str
  

print(mul_str("beep", 3))

  
"""
Problem 8. Reverse string
Write a function with 1 parameter: a string S. It should create and return a string made of characters
from S in reverse order.
Examples:
reverse(&#39;Python&#39;) &#39;nohtyP&#39;
reverse(&#39;abcdef&#39;) &#39;fedcba&#39;
"""
print ("Problem 8")
def reverse(S):
   new_str = ""
   for i in range(len(S)):
      new_str += S[len(S) - i - 1]
      #new_str += S[-i - 1]
      #new_str += S[-1 - i]
      #new_str += S[-(i + 1)]
      #new_str += S[-(i + 1)]
      #new_str += S[-(i + 1)]
      #new_str += S[-(i + 1)]
      #new_str += S[-(i + 1)]





