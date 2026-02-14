def duplicate_words(word_list):
    # Create a new list to store the duplicated words
    new_list = []
    
    # Iterate through each word in the original list
    for word in word_list:
        # Add the word twice to the new list
        new_list.append(word)
        new_list.append(word)
    
    # Print the new list as requested
    print(new_list)
    return new_list

# Test the function
original = ["apple", "banana", "cherry"]
print("Original list:", original)
print("New duplicated list:")
duplicate_words(original)
print("Original list after function (should be unchanged):", original)
