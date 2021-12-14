"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""


def hasCycle(graph, v, visited, dfsStack):
    pass


import collections


def canFinish(numCourse, prerequisites):
    # 0 : unlearned, 1: learning, 2: learned
    course_status = [0] * numCourse

    adv_dict = collections.defaultdict(list)

    for adv, base in prerequisites:
        adv_dict[base].append(adv)

    def dfs(course):
        if course_status[course] == 2:
            return True
        if course_status[course] == 1:
            return False
        # start to learn this course
        course_status[course] = 1
        for adv in adv_dict[course]:
            if not dfs(adv):
                return False
        # mark this course in learned
        course_status[course] = 2
        return True

    for course in range(numCourse):
        if not dfs(course): return False

    return True





numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))