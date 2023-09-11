import sys

def dijkstra(start, graph, distances):
    n = len(graph)
    visited = [False] * n
    distances[start] = 0

    for _ in range(n):
        min_dist = sys.maxsize
        min_node = -1

        # Find the unvisited node with the minimum distance
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                min_node = i

        if min_node == -1:
            break

        visited[min_node] = True

        # Update distances of neighboring nodes
        for neighbor, weight in graph[min_node]:
            if distances[min_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_node] + weight


def minimumWeight(n, edges, C1, C2):
    # Create directed graph from the array given in input
    graph = [[] for _ in range(n)]

    for i in range(n):
        for neighbor in edges[i]:
            if neighbor != -1:
                graph[i].append((neighbor, 1))

    # Create two lists A and B for storing min distance from C1 and C2
    A = [sys.maxsize] * n
    B = [sys.maxsize] * n

    # Part 1 and Part 2 of Algorithm -> Implement Dijkstra's algorithm for both arrays A and B
    dijkstra(C1, graph, A)
    dijkstra(C2, graph, B)

    # Now comes Part 3 of Algorithm -> Loop through and get node with min(A[i]+B[i])
    node = 0
    dist = sys.maxsize

    for i in range(n):
        # If node is not accessible from any of them, ignore it
        if A[i] == sys.maxsize or B[i] == sys.maxsize:
            continue

        if dist > A[i] + B[i]:
            dist = A[i] + B[i]
            node = i

    return node


# Test example
n = 23
edges = [[4], [4], [1], [4], [13], [8], [8], [8], [0], [8], [14], [9], [15], [11], [-1], [10], [15], [22], [22], [22], [22], [22], [21]]
C1 = 9
C2 = 2

result = minimumWeight(n, edges, C1, C2)
print(result)
