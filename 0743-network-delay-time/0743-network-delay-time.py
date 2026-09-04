import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = [[] for _ in range(n + 1)]

        for u, v, time in times:
            graph[u].append((v, time))

        distance = [float('inf')] * (n + 1)
        distance[k] = 0

        heap = [(0, k)]

        while heap:

            time, node = heapq.heappop(heap)

            if time > distance[node]:
                continue

            for next_node, edge_time in graph[node]:

                new_time = time + edge_time

                if new_time < distance[next_node]:
                    distance[next_node] = new_time
                    heapq.heappush(heap, (new_time, next_node))

        answer = max(distance[1:])

        if answer == float('inf'):
            return -1

        return answer