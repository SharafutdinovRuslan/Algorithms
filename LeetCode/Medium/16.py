from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        answer = nums[0] + nums[1] + nums[2]

        for i in range(n-2):
            j = i + 1
            k = n - 1

            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if abs(target - tmp) < abs(target - answer):
                    answer = tmp

                if tmp > target:
                    k -= 1
                elif tmp == target:
                    return target
                else:
                    j += 1

        return answer


if __name__ == "__main__":
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))

