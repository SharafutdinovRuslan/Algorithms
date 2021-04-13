class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            number = x % 10
            answer = answer*10 + number
            x = x // 10

        if answer > 2**31-1 or answer < -2**31:
            return 0

        return sign*answer


if __name__ == "__main__":
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
    print(Solution().reverse(0))
    print(Solution().reverse(1534236469))
