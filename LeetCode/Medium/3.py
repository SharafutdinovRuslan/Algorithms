class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        answer = 0
        hash_map = dict()
        n = len(s)
        i = 0

        for j in range(n):
            if s[j] in hash_map:
                i = max(i, hash_map[s[j]] + 1)

            answer = max(answer, j - i + 1)
            hash_map[s[j]] = j

        return answer


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring(""))
    print(Solution().lengthOfLongestSubstring("dvdf"))
    print(Solution().lengthOfLongestSubstring("abba"))
