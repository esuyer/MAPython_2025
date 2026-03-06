
user_word = input("Enter a word: ")

if len(user_word) > 0:
    
    first_char = user_word[0].lower()
    last_char = user_word[-1].lower()

    if first_char == last_char:
        print(f"The word '{user_word}' starts and ends with the same letter.")
    else:
        print(f"The word '{user_word}' does not start and end with the same letter.")

    
    print(user_word.upper())