class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for i in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)

        visited = [0] * numCourses

        def dfs(course):

            if visited[course] == 1:
                return False

            if visited[course] == 2:
                return True

            visited[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            visited[course] = 2

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True