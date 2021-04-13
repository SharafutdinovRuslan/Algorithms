from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = []

        for i in range(len(nums) - 1):
            target = -nums[i]
            numbers_set = set()
            for j in range(i+1, len(nums)):
                value = target - nums[j]
                if value in numbers_set:
                    new_answer = [nums[i], value, nums[j]]
                    new_answer.sort()
                    if new_answer not in answer:
                        answer.append(new_answer)
                else:
                    numbers_set.add(nums[j])

        return answer


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([]))
    print(Solution().threeSum([0]))
    print(Solution().threeSum([0, 0]))
