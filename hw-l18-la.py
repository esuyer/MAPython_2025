word = input("give me a string: ")
word = word.replace("a", "")
print("thanks for the a's:", word)
print("next")
def combination(code):
  code = str(code)
  if code.__len__() == 6 and code[0] == code[-1] and int(code[3]) % 2 == 0 and int(code[4]) + int(code[5]) == 10:
    return True
  else:
    return False
inputcode = int(input("i have a safe with these rules for the password: its 6 digits long; the first and last digits are the same; the 4th digit is even; and the sum of the 5th and 6th digits are equal. give me a code: "))
print("that code is", combination(inputcode))
print("next")



alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upperalpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "_", "=", "{", "[", "]", "}", "|", "'", '"', ":", ";", ",", ".", "/", "<", ">", "?", "`", "~"]
def decode(text = "", shift = 1):
  decoded = ""
  if text == "secretmessage123":
    print("oh cool, you unlocked the seceret part of this!")
    text2 = input("what do you actually want to decode: ")
    shift2 = int(input("whats the actuall shift: "))
    reps = int(input("how many times do you want to repeat decoding it: "))
    for ii in range(reps):
      decoded = ""
      for i in text2:
        letter = i
        if i in alphabet:
          letter = alphabet[(alphabet.index(letter) - (shift2 * ii)) % 26]
        elif i in digits:
          letter = digits[(digits.index(letter) - (shift2 * ii)) % 10]
        elif i in symbols:
          letter = symbols[(symbols.index(letter) - (shift2 * ii)) % 31]
        elif i in upperalpha:
          letter = upperalpha[(upperalpha.index(letter) - (shift2 * ii)) % 26]
        decoded += letter
      print(decoded)
    return "in all " + decoded
  else:
    for i in text:
      letter = i
      if i in alphabet:
        letter = alphabet[(alphabet.index(letter) - shift) % 26]
      elif i in digits:
        letter = digits[(digits.index(letter) - shift) % 10]
      elif i in symbols:
        letter = symbols[(symbols.index(letter) - shift) % 31]
      elif i in upperalpha:
        letter = upperalpha[(upperalpha.index(letter) - shift) % 26]
      decoded += letter
    return decoded
print("the decoded phrase is", decode(input("what do you want to decode: "), int(input("whats the shift: "))))

print("next")
print("uhh")
