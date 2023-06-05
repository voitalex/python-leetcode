""" 0015. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

Constraints:
  * 3 <= nums.length <= 3000
  * -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    """ 3Sum """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ Решение задачи """

        result = []

        if len(nums) < 3:
            return result

        nums.sort()

        for i in range(len(nums) - 2):

            # Пропускаем повторяющиеся решения
            if i == 0 or nums[i] > nums[i - 1]:

                negate = - nums[i]
                start, end = i + 1, len(nums) - 1

                while start < end:

                    # Три числа удовлетворяют условию задачи
                    if nums[start] + nums[end] == negate:
                        result.append([nums[i], nums[start], nums[end]])
                        start += 1
                        end -= 1

                        # Пропускаем повторяющиеся решения

                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1

                        while start < end and nums[start] == nums[start - 1]:
                            start += 1

                    # Сдвигаем левую границу, так как сумма оставшихся чисел меньше первого
                    elif nums[start] + nums[end] < negate:
                        start += 1

                    else:
                        end -= 1

        return result

print(
    Solution().threeSum([-2, 0, 1, 1, 2])
)