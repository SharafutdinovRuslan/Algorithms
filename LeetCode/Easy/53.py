from typing import List


"""
[-2, 1, -3, 4, -1, 2, 1, -5, 4]

пусть ответ s[i:j], тогда не существует i <= k <= j такого, что sum(s[i:k]) < 0 иначе может отбросить

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        answer = 0
        current_sum = 0

        for x in nums:
            current_sum = max(0, current_sum + x)
            answer = max(answer, current_sum)
        return answer
