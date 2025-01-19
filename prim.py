# parse input
N, M = map(int, input().split())

# init
graph = {}
minEdge = (None, None, float('inf'))

# build graph, storing minimum edge
for _ in range(M):
    u, v, w = map(int, input().split())
    
    if w < minEdge[2]:
        minEdge = (u, v, w)

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append((v, w))
    graph[v].append((u, w))

# build mst


mstNodes = {minEdge[0], minEdge[1]}
mst = {
    minEdge[0]: [(minEdge[1], minEdge[2])],
    minEdge[1]: [(minEdge[0], minEdge[2])]
}

minEdge = (None, None, float('inf'))
while len(mst) != (2*M - 1):
    for node in mstNodes:
        for v in graph[node]:
            if (v[0] != mst[node][0][0]) and (v[1] < minEdge[2]):
                minEdge = (node, v[0], v[1])

    # update mst
    if minEdge[0] not in mst:
        mst[minEdge[0]] = []
    if minEdge[1] not in mst:
        mst[minEdge[1]] = []

    mst[minEdge[0]].append((minEdge[1], minEdge[2]))
    mst[minEdge[1]].append((minEdge[0], minEdge[2]))

    # update mstNodes
    mstNodes.add(minEdge[0])
    mstNodes.add(minEdge[1])


            


print('end')