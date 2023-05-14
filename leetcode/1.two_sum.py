"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
"""

from typing import List

# First Way
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]==target-nums[j]:
                    return [j,i]


# Second Way
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             el = target - nums[i]
#             if el in hashmap:
#                 return [i, hashmap[el]]
#             hashmap[nums[i]] = i


result = Solution().twoSum(nums=[3,5,1,4,-8], target=5)
print(f"{result=}")