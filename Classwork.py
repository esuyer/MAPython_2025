nums = [5, 6, 6, 10]
def bob_is_right(nums):
  for i in range(len(nums) - 1):
      if nums[i] >= nums[i + 1]:
          return True
  return False
nums1 = [10, 100, 3000]
def bob_is_right(nums1):
    for i in range(len(nums1) - 1):
        if nums1[i] >= nums1[i + 1]:
            return True
    return False
nums2 = [1, 2, 3, 4, 2]
def bob_is_right(nums2):
      for i in range(len(nums2) - 1):
          if nums2[i] >= nums2[i + 1]:
              return True
      return False
print(bob_is_right(nums))
print(bob_is_right(nums1))
print(bob_is_right(nums2))
nums3 = [1, 1, 2, 1, 1]
def bob_is_right(nums3):
      for i in range(len(nums3) - 1):
          if nums3[i] >= nums3[i + 1]:
              return True
      return False
nums4 = [2, 1, 1, 2, 1]
def bob_is_right(nums4):
      for i in range(len(nums4) - 1):
          if nums4[i] >= nums4[i + 1]:
              return True
      return False
nums7 = [1, 1, 1, 2,1]
def bob_is_right(num7):
      for i in range(len(num7) - 1):
          if num7[i] >= num7[i + 1]:
              return True
nums5 = [10, 10]
def bob_is_right(nums5):
      for i in range(len(nums5) - 1):
          if nums5[i] >= nums5[i + 1]:
              return True
      return False
nums6 = [5]
def bob_is_right(nums6):
      for i in range(len(nums6) - 1):
          if nums6[i] >= nums6[i + 1]:
              return True
      return False
print(bob_is_right(nums4))
print(bob_is_right(nums5))
print(bob_is_right(nums6))
print(bob_is_right(nums7))
# Problem 1: Sum of positive numbers
def sum_positive(nums):
    total = 0
    for num in nums:
        if num > 0:
            total += num
    print("Sum of positives:", total)


# Problem 2: Multiple of 7
def has_multiple_of_7(nums):
    for num in nums:
        if num % 7 == 0:
            print("Multiple of 7:", True)
            return
    print("Multiple of 7:", False)


# Problem 3: Smallest number
def smallest_number(nums):
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    print("My algorithm:", smallest)
    print("Function min:", min(nums))


# Problem 4: Words starting with 'a'
def count_a_words(words):
    count = 0
    for word in words:
        if word[0] == 'a':
            count += 1
    print("Words starting with 'a':", count)


# Problem 5: Length of longest word
def longest_length(words):
    max_len = len(words[0])
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    print("Longest length:", max_len)


# Problem 6: Longest word
def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    print("Longest word:", longest)
    print("Length:", len(longest))


# Problem 7: find (first occurrence)
def find(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


# Problem 8: right_find (last occurrence)
def right_find(lst, value):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            return i
    return -1


# ------------------ TESTS ------------------

sum_positive([10, -50, 1000, -7, -999, 700])

has_multiple_of_7([10, 0, 1000, -14, -999, 700])

smallest_number([3, 1, -10, 17])

count_a_words(['avocado', 'cat', 'at', 'archer', 'zebras'])

longest_length(['buzz', 'Python', 'cat', 'at', 'zebras'])

longest_word(['buzz', 'python', 'cat', 'zebras'])

print("find:", find(['dog', 'python', 'cat', 'zebra', 'cat'], 'cat'))

print("right_find:", right_find(['dog', 'python', 'cat', 'zebra', 'cat'], 'cat'))