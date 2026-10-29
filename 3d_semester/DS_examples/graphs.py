"""
Цепь - маршрут без повторяющихся ребер.
Простая цепь - маршрут без повторяющихся вершин.
Цикл - цепь, в которой первая и последняя вершины совпадают.

примеры:

AB - BC - CD - DE простая цепь (=> и обычная), так как нет повторов вершин
AB - BC - CD - DE - EB просто цепь, но не простая, так как есть повтор вершины B, а все ребра уникальны
AB - BC - CD - DE - EB - BC не цепь, так как повтор ребра BC
AB - BC - CD - DE - EA - цикл, так как начало == конец == А
цикл это не простая цепь, так как есть повтор вершины А
"""



# dfs - Depth First Search, recurrent
def do_dfs(graph):

    def dfs(graph, current):
        visited.add(current)
        print(current)

        for next in graph[current] - visited:
            dfs(graph, next)

    visited = set()

    for vertex in graph.vertexes():   #graph class method for getting vertexes
        if vertex not in visited:
            dfs(graph, vertex)


# bfs - Breadth First Search
def do_bfs(graph, start):
    level = [-1] * graph.size()
    level[start] = 0
    q = [start]  # queue using list (for optimization: list -> deque)

    while q:
        current = q.pop(0)
        for neighbour in current.get_neighbours():
            if level[neighbour] == -1:  # not visited yet
                q.append(neighbour)
                level[neighbour] = level[current] + 1


import heapq
def dijkstra(graph: dict, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances