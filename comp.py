def is_interesting(word):
  lower = word.lower()
  if lower == "interesting":
    return True
  if "x" in lower and "y" in lower:
    return True
  if lower[0] == lower[-1]:
    return True
  return False

print(is_interesting("Interesting"))
print(is_interesting("INTERESTING"))
print(is_interesting("foxy"))
print(is_interesting("level"))
print(is_interesting("python"))
print(is_interesting("xylophone"))