'''
  Problem 1. Remove short words
  Given a list of words, remove from it all the words that have less than 5 letters. Do not create any new
  lists. Use one of the algorithms from class.
  Examples:
  remove_short([&#39;table&#39;, &#39;book&#39;, &#39;at&#39;, &#39;cupboard&#39;])  [&#39;table&#39;, &#39;cupboard&#39;]
  remove_short([&#39;I&#39;, &#39;like&#39;, &#39;cake&#39;])  []
  '''
def remove_short(words):
  i = 0
  while i < len(words):
    if len(words[i]) < 5:
      words.pop(i)
      i -= 1

    i += 1

  print(words)
  
  '''
  Problem 2. Alarm clock
  This problem is from CodingBat
  Given a day of the week encoded as 1=Sun, 2=Mon, 3=Tue, ...7=Sat, and a True/False
  value indicating if we are on vacation, print a string in format &#39;7:00&#39; indicating when the
  alarm clock should ring.
  Weekdays, the alarm should be &#39;7:00&#39; and on the weekend it should be &#39;10:00&#39;.
  Unless we are on vacation - then on weekdays it should be &#39;10:00&#39; and on weekends it
  should be &#39;off&#39;.
  Examples:
  alarm(2, False)  &#39;7:00&#39;
  alarm(6, False)  &#39;7:00&#39;
  alarm(1, False)  &#39;10:00&#39;
  alarm(2, True)  &#39;10:00&#39;
  alarm(7, True)  &#39;off&#39;
  '''
  print("Problem 2")
  
  def alarm(day, vacation):
    if vacation:
      if day == 1 or day == 7:
        print("off")
      else:
        print("10:00")

    else:
      if day == 1 or day == 7:
        print("10:00")

      else:
        print("7:00")

  alarm(2, False)
  alarm(6, False)
  
  

'''
  Problem 3. Repeat separator
  This problem is from CodingBat
  Write a function with 3 parameters: two strings – word and separator, and an integer N. This function
  should create and return a new string made of N repetitions of word separated by separator.
  Examples:
  
  repeat_sep(&#39;This&#39;, &#39;And&#39;, 3)  &#39;ThisAndThisAndThis&#39;
  repeat_sep(&#39;That&#39;, &#39;Or&#39;, 1)  &#39;That&#39;
  repeat_sep(&#39;Ha&#39;, &#39;-&#39;, 5)  &#39;Ha-Ha-Ha-Ha-Ha&#39;
  repeat_sep(&#39;Ha&#39;, &#39;-&#39;, 0)  &#39;&#39;
  '''
print("Problem 3")

def repeat_sep(word, sep, n)
  result = ""
  for i in range(n):
    result += word
    if i < n - 1:
      result += sep

  print(result)

'''
  Problem 4. Neighbors
  There are several houses on the street. You are given a list of the last names of
  the families living in these houses. For each family in the list print the names of
  their neighbors like in the example below.
  Note that you only need to print the information if a family has both neighbors.
  Examples:
  List of names Output
  [&#39;Jacksons&#39;, &#39;Smiths&#39;, &#39;Foremans&#39;, &#39;Blooms&#39;,
  &#39;Lees&#39;]

  Smiths live between Jacksons and Foremans
  Foremans live between Smiths and Blooms
  Blooms live between Foremans and Lees
  [&#39;Simpsons&#39;, &#39;Millers&#39;, &#39;Potters&#39;] Millers live between Simpsons and Potters
  [&#39;Johnsons&#39;, &#39;Bensons&#39;]
'''
print("Problem 4")

names = ['Jacksons', 'Smiths', 'Foremans', 'Blooms', 'Lees']
for i in range(1, len(names) - 1):
  print(names[i] + " live between " + names[i - 1] + " and " + names[i + 1])

  


  
 
  '''
  Problem 5. Fancy string
  Given a list of integers, create a string made of &#39;&lt;&#39;, &#39;&gt;&#39;, and &#39;=&#39; characters that shows how the numbers
  change from one to another in this list. The rules for creating this string are as follows:
  for every pair of numbers in the list that are next to each other
  - add &#39;&lt;&#39; to the string if the 1 st number in the pair is smaller than the 2 nd
  - add &#39;&gt;&#39; to the string if the 1 st number in the pair is greater than the 2 nd
  - add &#39;=&#39; to the string both the numbers in the pair are the same
  For example,

  Examples:
  fancy_string([3, 3, 3, 3])  &#39;===&#39;
  fancy_string([0, 1, 2, 3, 4, 5]) &#39;&lt;&lt;&lt;&lt;&lt;&#39;
  fancy_string([3, 3, 10, -5, 2])  &#39;=&lt;&gt;&lt;&#39;
  Tips: the string should start empty.
  If stuck, start with writing code that loops through the list and prints pairs of numbers – the current
  and the next.
  '''
  def fancystring(numbers):
     result = ""
     for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
           result += "<"
        elif numbers[i] > numbers[i + 1]:
           result += ">"
        else:
           result += "="
          
     print(result)

  fancystring([3, 3, 3, 3])
  

