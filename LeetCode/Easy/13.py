class Solution:

    roman_symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        answer = 0

        for i in range(len(s)-1):
            if self.roman_symbols[s[i]] < self.roman_symbols[s[i+1]]:
                answer -= self.roman_symbols[s[i]]
            else:
                answer += self.roman_symbols[s[i]]

        answer += self.roman_symbols[s[len(s)-1]]

        return answer


if __name__ == "__main__":
    print(Solution().romanToInt("III"))
    print(Solution().romanToInt("IV"))
    print(Solution().romanToInt("IX"))
    print(Solution().romanToInt("LVIII"))
    print(Solution().romanToInt("MCMXCIV"))