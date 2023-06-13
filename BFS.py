def bfs(graph, goal):

    startNode = list(graph.keys())[0]
    queue, temp, path, visited = [startNode], [], [], []
    parent = {startNode: None}

    while queue:

        v = queue.pop(0)
        if v in visited:
            continue

        visited.append(v)
        if v == goal:
            node = goal
            while parent[node]:
                path.insert(0, node)
                node = parent[node]
            path.insert(0, startNode)
            break

        for i in graph.get(v, []):
            if i not in visited:
                queue.append(i)
                parent[i] = v

    if not path:
        path = "there is no path because goal not found"

    return path, visited


graph = {1: [2, 3], 2: [5, 6], 3: [7, 8], 5: [9],
         6: [10, 11], 7: [12, 13], 8: [14]}

path, visited = bfs(graph, 10)
print("path :", path, "\n", "visited nodes :", visited)
