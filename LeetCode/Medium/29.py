class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0:
            if divisor > 0:
                sign = -1
        else:
            if divisor < 0:
                sign = -1

        answer = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        increment = divisor

        while divisor <= dividend:
            answer += 1
            divisor += increment

        answer = answer if sign == 1 else -answer
        if answer < -2**31:
            answer = -2**31
        elif answer > 2**31 - 1:
            answer = 2**31 - 1

        return answer


if __name__ == "__main__":
    print(Solution().divide(10, 3))
    print(Solution().divide(7, -3))
    print(Solution().divide(0, 1))
    print(Solution().divide(1, 1))
