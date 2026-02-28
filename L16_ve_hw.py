def even_to_dot(g):
  new_st=""
  for i in range (len(g)):
      if i % 2==1:
        new_st+=""
      else:
        new_st+=g[i]

  return new_st
print(even_to_dot('python'))

def double_letters(h):
   new_str=""
   for i in range (len(h)):
     new_str+=h[i] * 2

   return new_str

print(double_letters('hi'))