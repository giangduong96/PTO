"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.



Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.


1 <= n <= 105
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.
"""


def numOfMinnutes(number: int, headID: int, manager: list, informTime: list):
    tree = {}

    for employ_id, m in enumerate(manager):
        if m == -1:
            continue
        elif m not in tree:
            tree[m] = [employ_id]
        else:
            # add employee to manager list
            tree[m] += [employ_id]
    print(tree)
    ans = 0
    queue = [(headID, 0)]
    print("que", queue)
    while queue:
        employee_id, time = queue.pop(0)
        ans = max(ans, time)
        if employee_id in tree:
            for subordinate in tree[employee_id]:
                queue += [(subordinate, time + informTime[employee_id])]
        print(queue, ans)
    return ans




n = 6
headID = 2
manager = [2, 2, -1, 2, 2, 2]
informTime = [0, 0, 1, 0, 0, 0]

mm = numOfMinnutes(n, headID, manager, informTime)
print(mm)
# n = 7
# headID = 6
# manager = [1,2,3,4,5,6,-1]
# informTime = [0,6,5,4,3,2,1]
# print(numOfMinnutes(n, headID, manager, informTime))


