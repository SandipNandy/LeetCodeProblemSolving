
"""Leetcode Question 22: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]
"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        res = []
        backtrack()
        return res
n1 = 2


solver1 = Solution()
output1 = solver1.generateParenthesis(n1)
print(f"Input: n = {n1}")
print(f"Output: {output1}")







