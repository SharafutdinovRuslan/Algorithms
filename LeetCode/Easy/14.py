from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        prefix = ""
        iteration_range = min(len(strs[0]), len(strs[1]))
        j = 0
        while j < iteration_range and strs[0][j] == strs[1][j]:
            prefix += strs[0][j]
            j += 1

        for i in range(2, len(strs)):
            j = 0
            iteration_range = min(len(prefix), len(strs[i]))
            while j < iteration_range and prefix[j] == strs[i][j]:
                j += 1

            prefix = prefix[:j]

            if len(prefix) == 0:
                break

        return prefix


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
