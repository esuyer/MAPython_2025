def horse_before_cart(words):
  new_list = []
  for word in words:
      if word == "cart":
          new_list.append("horse")
      new_list.append(word)
  print(new_list)
  return new_list
example_words = ["apple", "cart", "banana", "cart", "dog", "cart"]
print(f"Original list: {example_words}")
print("New list with horses:")
horse_before_cart(example_words)
