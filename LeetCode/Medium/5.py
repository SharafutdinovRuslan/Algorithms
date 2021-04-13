class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        start = 0
        end = 1
        max_palindromic_length = 1

        """
        P(i, j) = P(i + 1, j - 1)  and s(i) == s(j)
        P(i, i + 1) = 1 if s(i) == s(i+1)
        """

        for i in range(n - 1):
            matrix[i][i] = 1
            if s[i] == s[i+1]:
                matrix[i][i+1] = 1
                max_palindromic_length = 2
                start = i
                end = i + 2
            else:
                matrix[i][i+1] = 0
        matrix[n-1][n-1] = 1

        for i in range(2, n):
            for j in range(0, n-i):
                if s[j] == s[j+i]:
                    matrix[j][j+i] = matrix[j+1][j+i-1]
                    if matrix[j][j+i] == 1 and i + 1 > max_palindromic_length:
                        max_palindromic_length = i + 1
                        start = j
                        end = j + i + 1
                else:
                    matrix[j][j+i] = 0

        # for i in range(n):
        #     print(*matrix[i])
        #
        # print(start, end)

        return s[start:end]


if __name__ == "__main__":
    # print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("ac"))
