"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         print(nums)
#         for i in range(len(nums)):
#             if nums[i] in nums[i+1:]:
#                 print(True)
#         print(False)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num2 = set(nums)
        l1 = len(nums)
        l2 = len(num2)

        if l1!=l2:
           return True
        else:
            return False
    
    
Solution.containsDuplicate(Solution, [1,2,3,1])
Solution.containsDuplicate(Solution, [1,2,3,4])
Solution.containsDuplicate(Solution, [1,1,1,3,3,4,3,4,2,2])