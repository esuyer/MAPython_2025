print("\nQuestion 1\n")
def aA_to_Z(aA_to_Z):
  aA_to_Z= ('pkAirea')
  aA_to_Z = aA_to_Z.replace('a', 'z')
  aA_to_Z = aA_to_Z.replace('A', 'z')
  return aA_to_Z
print(aA_to_Z(aA_to_Z))
print("\nQuestion 2\n")
K= ("Kazuya Mishima Wins!!")
def K1(K):
  i = 0
  result=""
  for letter in K:
     if i %2 == 0:
       result += "."
     else:
       result += letter
  i += 1
  return result
print(K1(K))
print("\nQuestion 3\n")
def del_aA(del_aA):
  del_aA= ('pkAFirea')
  del_aA = del_aA.removesuffix('a')
  del_aA = del_aA.removesuffix('A')
  return del_aA
print(del_aA(del_aA))