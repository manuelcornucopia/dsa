from graph import Graph


def dijkstra(graph: Graph, src, dst=None):
    dist = {v: float("inf") for v in graph.graph}
    dist[src] = 0
    prev = {}

    pq = MinPriorityQueue()
    pq.push(0, (src, 0))

    while not pq.is_empty():
        u, du = pq.pop()
        if du != dist[u]:
            continue

        if dst is not None and u == dst:
            break

        neighbors = graph.graph.get(u, [])
        if graph.weighted:
            edges = neighbors
        else:
            edges = [(v, 1) for v in neighbors]

        for v, w in edges:
            alt = du + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                pq.push(alt, (v, alt))

    return dist, prev


def reconstruct_path(prev, src, dst):
    if src == dst:
        return [src]
    if dst not in prev:
        return []
    path = [dst]
    while path[-1] != src:
        path.append(prev[path[-1]])
    path.reverse()

    return path
