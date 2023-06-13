def dfs(graph, goal, limit):

    startNode = list(graph.keys())[0]
    stack, temp, path, visited = [(startNode, 1)], [], [], []
    parent = {startNode: None}

    while stack:

        v, d = stack.pop()
        visited.append(v)

        if v == goal:
            node = goal
            while parent[node]:
                path.insert(0, node)
                node = parent[node]
            path.insert(0, startNode)
            break

        for i in graph.get(v, []):
            if d < limit and i not in visited:
                temp.append((i, d+1))
                parent[i] = v
        while temp:
            stack.append(temp.pop())

    if not path:
        path = "there is no path because goal not found"

    return path, visited


graph = {1: [2, 3], 2: [5, 6], 3: [7, 8], 5: [9],
         6: [10, 11], 7: [12, 13], 8: [14]}

maxDepth = 5
for i in range(1, maxDepth):
    path, visited = dfs(graph, 8, i)
    if path == "there is no path because goal not found":
        continue
    else:
        print("path :", path, "\n", "visited nodes :",
              visited, "\n", "found in level : ", i)
        break
