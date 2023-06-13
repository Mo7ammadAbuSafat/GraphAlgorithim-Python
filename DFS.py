def dfs(graph, goal):

    startNode = list(graph.keys())[0]
    stack, temp, path, visited = [startNode], [], [], []
    parent = {startNode: None}

    while stack:

        v = stack.pop()
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
                temp.append(i)
                parent[i] = v
        while temp:
            stack.append(temp.pop())

    if not path:
        path = "there is no path because goal not found"

    return path, visited


graph = {1: [2, 3], 2: [5, 6], 3: [7, 8], 5: [9],
         6: [10, 11], 7: [12, 13], 8: [14]}

path, visited = dfs(graph, 9)
print("path :", path, "\n", "visited nodes :", visited)
