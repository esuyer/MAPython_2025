print("Question 1\n")
List= [10, -50, 1000, -7, -999, 700]
def sum_of_positives_loop(numbers):
    total = 0 
    for number in numbers:
        if number > 0:  
            total += number  
    return total
result = sum_of_positives_loop(List)
print(f"List: {List}")
print(f"Sum of positive numbers: {result}")

print("\nQuestion 2\n")
def check_multiple_of_7_loop(numbers):
  for num in numbers:
    if num % 7 == 0:
      return True 
  return False 
list2 = [3, 10, 15, 28, 33]
print(f"List 2: {list2}")
print(f"List 2 contains a multiple of 7: {check_multiple_of_7_loop(list2)}")

print("\nQuestion 3\n")
def find_smallest_number(numbers):
  numeric_numbers = [float(x) for x in numbers]
  smallest_num = numeric_numbers[0]
  for num in numeric_numbers[1:]:
      if num < smallest_num:
          smallest_num = num

  return smallest_num

list1 = [3, 1, "-10", 17]
my_algorithm_result1 = find_smallest_number(list1)
function_min_result1 = min(list1, key=float)
print(f"Input: {list1}")
print(f"My algorithm: {my_algorithm_result1}")
print(f"Function min: {function_min_result1}")

print("\nQuestion 4\n")
