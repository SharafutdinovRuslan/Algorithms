from typing import List

"""
[0, 0, 1, 2, 2, 2, 3, 3, 4, 5, 5]
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 2]))
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
