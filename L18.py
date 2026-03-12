def encode (msg, shift):
    encoded = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",       "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",         "s", "t", "u", "v", "w", "x", "y", "z"]

    for letter in msg:
      if letter == " ":
          encoded = encoded + " "
          continue
      uppercase = letter.isupper()
      pos = alphabet.index(letter.lower())
      pos = pos + shift
      if pos >= len(alphabet):
          pos = pos - len(alphabet)
      if uppercase:
          encoded = encoded + alphabet[pos].upper()
      else:  
          encoded = encoded + alphabet[pos]
    
    return encoded

secret = encode("How much wood could a wood chuck chuck", 5)
print (secret)

