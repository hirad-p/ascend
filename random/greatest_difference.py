# http://blog.teamtreehouse.com/passing-google-interview-without-computer-science-degree

def greatest_difference(nums):
  minimum = float('inf') 
  maximum = float('-inf')
  for n in nums:
    if n < minimum:
      minimum = n
    elif n > maximum:
      maximum = n
  
  return maximum - minimum

nums = [5, 8, 6, 1]
difference = greatest_difference(nums)
print(nums, difference)