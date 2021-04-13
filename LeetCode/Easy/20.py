class Solution:
    def isValid(self, s: str) -> bool:

        brackets_map = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        stack = []
        stack_len = 0

        for bracket in s:
            if bracket in ("(", "{", "["):
                stack.append(bracket)
                stack_len += 1
            else:
                if stack_len > 0:
                    last_open_bracket = stack.pop()
                    stack_len -= 1
                    if bracket != brackets_map[last_open_bracket]:
                        return False
                else:
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
    print(Solution().isValid("([)]"))
    print(Solution().isValid("{[]}"))
    print(Solution().isValid("(){}}{"))
