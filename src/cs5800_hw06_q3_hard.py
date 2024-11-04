class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # initialize stack to point the last element.
        max_len = 0  # initialize the maximum valid length of prantheses.

        for i in range(len(s)):  # loop through a given string.
            if s[i] == "(":
                stack.append(i)  # record the index on stack[-1].
            else:  # s[i] = ")"
                stack.pop()  # remove the index stored on stack[-1], since the prantheses had ended.
                if len(stack) == 0:  # if stack is empty.
                    stack.append(i)  # avoid stack being empty.
                else:  # stack is not empty, means there is previous "(" appearing before current ")"
                    max_len = max(
                        max_len, i - stack[-1]
                    )  # compare previous valid prantheses and the current valid prantheses
        return max_len


if __name__ == "__main__":
    s = ")()())"
    sol = Solution().longestValidParentheses(s)
    print(sol)
