class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output_strings = ["" for _ in range(numRows)]
        n = len(s)
        i = 0

        while i < n:

            for j in range(numRows):
                if i == n:
                    break
                output_strings[j] += s[i]
                i += 1

            for j in range(numRows-2, 0, -1):
                if i == n:
                    break
                output_strings[j] += s[i]
                i += 1

        return "".join(output_strings)


if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 3))
