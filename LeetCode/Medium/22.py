from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def parenthesis(s, left, right):
            if len(s) == 2 * n:
                answer.append(s)
                return
            if left < n:
                parenthesis(s + '(', left+1, right)
            if right < left:
                parenthesis(s + ')', left, right+1)

        parenthesis('', 0, 0)

        return answer


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
