""" 0268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
    Input: nums = [3,0,1]
    Output: 2

Example 2:
    Input: nums = [0,1]
    Output: 2

Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8

Constraints:
  * n == nums.length
  * 1 <= n <= 104
  * 0 <= nums[i] <= n
  * All the numbers of nums are unique.
"""

from typing import List


class Solution:
    """ Missing Number """

    def missingNumber(self, nums: List[int]) -> int:
        """ Решение задачи """

        nums_count = len(nums) + 1
        nums_sum = (nums_count * (nums_count - 1)) // 2

        for num in nums:
            nums_sum -= num

        return nums_sum
