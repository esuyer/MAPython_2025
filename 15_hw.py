def duplicatewords(word_list):
  newlist = []

  for word in word_list:
      newlist.append(word)
      newlist.append(word)

  print(newlist)
  return newlist

original = ["apple", "banana", "cherry"]
print("Original list:", original)
print("New duplicated list:")
duplicatewords(original)

