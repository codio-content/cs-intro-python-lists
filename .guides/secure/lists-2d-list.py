import subprocess
import sys

student_file = "code/lists/2d_exercise.py"
student_output = subprocess.check_output(["python3", student_file]).rstrip().decode("utf-8")
with open(student_file, "r") as code:
  student_code = code.readlines()
expected_output = "[[12, 11, 10], [9, 8, 7], [6, 5, 4], [3, 2, 1]]"

def check_output(student_output, expected_output):
  result = student_output == expected_output
  if result == False:
    print("Your program did not have the expected output")
  return result

def check_reverse(file):
  has_reverse = False
  for line in file:
    if "reverse" in line:
      has_reverse = True
  if has_reverse == False:
    print("Your program did not use the 'reverse' method")
  return has_reverse

def check_sort(file):
  has_sort = False
  for line in file:
    if "sort" in line:
      has_sort = True
  if has_sort == False:
    print("Your program did notuse the 'sort' method")
  return has_sort

def check_numbers(file):
  unchanged_numbers = False
  expected_numbers = "numbers = [[3, 1, 2], [8, 7, 9], [10, 12, 11], [4, 5, 6]]"
  for line in file:
    if expected_numbers in line:
      unchanged_numbers = True
  if expected_numbers == False:
    print("The initial value of 'numbers' should not be changed")
  return unchanged_numbers

test1 = check_output(student_output, expected_output)
# test2 = check_reverse(student_code)
# test3 = check_sort(student_code)
test4 = check_numbers(student_code)

if test1 and test4:
  print("Test passed!")
  sys.exit(0)
else:
  sys.exit(1)
