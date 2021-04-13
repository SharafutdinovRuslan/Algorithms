from typing import List

"""
[0, 1, 2, 2, 3, 0, 4, 2]

swap_index = 7
i = 2
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap_index = len(nums) - 1
        i = 0

        while i < swap_index + 1:
            if nums[i] == val:
                nums[i], nums[swap_index] = nums[swap_index], nums[i]
                swap_index -= 1
            else:
                i += 1

        return i


if __name__ == "__main__":
    print(Solution().removeElement([3, 2, 2, 3], 3))
    print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
    print(Solution().removeElement([1], 1))
