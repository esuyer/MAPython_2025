def rook_attack(row1,col1,row2,col2):
   if row1==row2 or col1==col2:
     return True
   else:
      return False

print(rook_attack(2,3,2,1))
print(rook_attack(3,1,8,2))