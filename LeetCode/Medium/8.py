class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        sign = 1
        output_number = 0

        while i < n and s[i] == " ":
            i += 1

        if i == n:
            return output_number

        if s[i] == "-":
            sign = -1
            i += 1
            if i == n or (not s[i].isdigit()):
                return output_number
        elif s[i] == "+":
            sign = 1
            i += 1
            if i == n or (not s[i].isdigit()):
                return output_number
        elif not s[i].isdigit():
            return output_number

        while i < n and s[i].isdigit():
            output_number *= 10
            output_number += (ord(s[i]) - ord('0'))
            i += 1

        output_number *= sign

        if (2 ** 31) - 1 >= output_number >= -2 ** 31:
            return output_number
        elif sign == 1:
            return (2 ** 31) - 1
        else:
            return -2 ** 31


if __name__ == "__main__":
    print(Solution().myAtoi("42"))
    print(Solution().myAtoi("   -42"))
    print(Solution().myAtoi("4193 with words"))
    print(Solution().myAtoi("words and 987"))
    print(Solution().myAtoi("-91283472332"))




