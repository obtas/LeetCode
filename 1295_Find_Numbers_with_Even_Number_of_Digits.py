"""
Given an array nums of integers, return how many of them contain an even number of digits.

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
"""

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        a = []
        b = []
        for i in nums:
            # print(i)
            counter = 0
            while i > 0:
                i //= 10
                counter += 1
            a.append(counter)
        # print(a)
        
        for i in a:
            if i % 2 == 0:
                # print(i)
                b.append(i)                
                # print(b)     
            else:
                pass
        return len(b)

            
Solution.findNumbers(Solution, [12,345,2,6,7896])
Solution.findNumbers(Solution, [12])