def remove_short(words):
  i = 0
  while i < len(words):
      if len(words[i]) < 5:
          words.pop(i)
      else:
          i += 1
  return words

def alarm(day, vacation):
  if vacation:
      if day == 1 or day == 7:
          return "off"
      else:
          return "10:00"
  else:
      if day == 1 or day == 7:
          return "10:00"
      else:
          return "7:00"

def repeat_sep(word, separator, n):
  result = ""
  for i in range(n):
      result += word
      if i < n - 1:
          result += separator
  return result

def neighbors(names):
  for i in range(1, len(names) - 1):
      print(names[i], "live between", names[i - 1], "and", names[i + 1])

def fancy_string(nums):
  result = ""
  for i in range(len(nums) - 1):
      if nums[i] < nums[i + 1]:
          result += "<"
      elif nums[i] > nums[i + 1]:
          result += ">"
      else:
          result += "="
  return result

print(remove_short(['table', 'book', 'at', 'cupboard']))
print(remove_short(['I', 'like', 'cake']))

print(alarm(2, False))
print(alarm(6, False))
print(alarm(1, False))
print(alarm(2, True))
print(alarm(7, True))

print(repeat_sep('This', 'And', 3))
print(repeat_sep('That', 'Or', 1))
print(repeat_sep('Ha', '-', 5))
print(repeat_sep('Ha', '-', 0))

neighbors(['Jacksons', 'Smiths', 'Foremans', 'Blooms', 'Lees'])
neighbors(['Simpsons', 'Millers', 'Potters'])
neighbors(['Johnsons', 'Bensons'])

print(fancy_string([3, 3, 3, 3]))
print(fancy_string([0, 1, 2, 3, 4, 5]))
print(fancy_string([3, 3, 10, -5, 2]))