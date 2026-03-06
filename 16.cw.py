def str_replace(A):
  new_str = ""
  for pos in range(len(A)):
    if A[pos] == 'A'or A[pos] =='a':
      new_str += ""
    else: 
      new_str += A[pos]
  return new_str
print(str_replace("BehSwamSimUlaTAr"))
