from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers_dict = dict()
        i = 0

        for elem in nums:
            value = target - elem
            if value not in numbers_dict:
                numbers_dict[elem] = i
            else:
                return [numbers_dict[value], i]
            i += 1


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 3], 6))
