"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""


# brute force

def generateParenetheses(num):
    def generate(A=[]):
        if len(A) == 2 * num:
            if valid(A):
                ans.append("..".join(A))

        else:
            global j
            j += 1
            A.append("(")
            generate(A)
            A.pop()
            A.append(')')
            generate(A)
            A.pop()

    def valid(A):
        balance = 0
        for c in A:
            if c == '(':
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    return False
        return balance == 0

    ans = []
    generate()
    return ans


# backtracking

def generateParenthesis2(num):
    ans = []

    def backtrack(S=[], left=0, right=0):
        if len(S) == 2 * num:
            ans.append("".join(S))
            # print(ans)

        if left < num:
            S.append("(")
            # print("left", S, left, right)
            backtrack(S, left + 1, right)
            S.pop()

        if right < left:
            S.append(")")
            # print("right", S, left,right)
            backtrack(S, left, right + 1)
            S.pop()

    backtrack()
    return ans


# closure number
def generateParenthesis3(num):
    if num == 0:
        return ['']
    ans = []
    for c in range(num):
        for left in generateParenthesis3(c):
            for right in generateParenthesis3(num - 1 - c):
                print(left, right)
                ans.append('({}){}'.format(left, right))
    return ans








print(generateParenthesis3(1))