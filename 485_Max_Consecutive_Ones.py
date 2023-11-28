"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.


"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        counter = 0
        new_list = []
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                new_list.append(counter)
                counter = 0
        new_list.append(counter)
        return max(new_list)


Solution.findMaxConsecutiveOnes(Solution, [1,1,0,1,1,1])