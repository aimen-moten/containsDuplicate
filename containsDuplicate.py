# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Solution to Leetcode 217
# ----------------

# Algorithm

# 1. Create a set of the array nums and compare both lengths to check if they match.
# 2. Alternatively, loop through the array to count the occurence of each number and return false is any number has a count over 1.

# Code:

# Option 1:
def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

# Option 2:
def containsDuplicate(nums: list[int]) -> bool:
    hashSet = {}
    for n in nums:
        if n in hashSet:
            return True
        hashSet[n] = 0
    return False

# Code for testing:
print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

# Time Complexity: O(N)
# Space Complexity: O(N) (approximately)