"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
"""


def valid(string):
    stack, lookup = [], {"{": "}", "(": ")", "[": "]"}
    for parenthesis in string:
        if parenthesis in lookup.keys():
            stack.append(parenthesis)
        elif len(stack) == 0 or lookup[stack.pop()] != parenthesis:
            return False
    return len(stack) == 0



s = "{[]}"
print(valid(s))

