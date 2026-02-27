def double_words(words):

    new_list = []
    for word in words:
        new_list.append(word)
        new_list.append(word)
    print(new_list)
    return new_list

example_words = ["apple", "cart", "banana", "cart", "dog", "cart"]
print(f"Original list: {example_words}")

print("\nTask: double_words")
double_words(example_words)

print(f"\nVerifying original list remains unchanged: {example_words}")
