from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        answer = 0

        for elem in nums:
            if target <= elem:
                break
            else:
                answer += 1

        return answer


if __name__ == "__main__":

    print(Solution().searchInsert([1, 3, 5, 6], 5))
    print(Solution().searchInsert([1, 3, 5, 6], 2))
    print(Solution().searchInsert([1, 3, 5, 6], 7))
    print(Solution().searchInsert([1, 3, 5, 6], 0))
    print(Solution().searchInsert([1], 0))
