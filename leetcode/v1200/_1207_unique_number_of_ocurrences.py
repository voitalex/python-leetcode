""" 1207. Unique Number of Occurrences

Link: https://leetcode.com/problems/unique-number-of-occurrences

Given an array of integers arr, write a function that returns true if and only if the number of occurrences
of each value in the array is unique.

Example 1:
    Input: arr = [1,2,2,1,1,3]
    Output: true
    Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
    Input: arr = [1,2]
    Output: false

Example 3:
    Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
    Output: true

Constraints:
    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
"""

import collections
from typing import List


class Solution:
    """ Unique Number of Occurrences """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """ Решение задачи """

        counter = collections.Counter(arr)
        unique_occurrences = set(counter.values())

        return len(unique_occurrences) == len(counter)
