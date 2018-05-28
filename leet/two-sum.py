# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
def two_sum(nums, target):
  needed = dict()
  for i in range(len(nums)):
    print(needed)
    
    difference = target - nums[i]
    print(target, nums[i], difference)
    
    if difference in needed:
      return [i, needed[difference]]
    else:
      needed[nums[i]] = i

nums = [2, 7, 11, 15]
target = 26
two_sums = two_sum(nums, target)
print(two_sums)

