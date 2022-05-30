""" 0001. Two Sum """

from typing import List


class Solution:
    """ Two Sums """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ Решение задачи """

        numbers_map = {value: index for index, value in enumerate(nums)}
        
        for index, value in enumerate(nums):
            left = target - value
            if (left_index := numbers_map.get(left, None)) is not None:
                if index != left_index:
                    return [index, left_index]

        return []
