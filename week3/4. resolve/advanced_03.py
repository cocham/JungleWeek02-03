import heapq


INF = float('inf')


def dijkstra(n: int, edges: list, start: int) -> list:
    """
    n: 정점 수 (정점 번호 0 ~ n-1)
    edges: (u, v, w) 형식 방향 간선 리스트
    start: 출발 정점
    반환: 길이 n 의 거리 리스트 (도달 불가 = float('inf'))
    """
    graph = [[] for _ in range(n)]

    for edge in edges:
        u = edge[0]
        v = edge[1]
        weight = edge[2]

        graph[u].append((v, weight))
    
    dists = [INF] * n
    dists[start] = 0
    
    heap = []
    heapq.heappush(heap, (start, 0))
    
    while (heap):
        cur_node, cur_w = heapq.heappop(heap)
        
        if (cur_w > dists[cur_node]):
            continue
        
        for next_node, w in graph[cur_node]:
            next_w = w + cur_w
            
            if (next_w < dists[next_node]):
                dists[next_node] = next_w
                heapq.heappush(heap, (next_node, next_w))
    
    return dists
    
        
    
    


def _format(dist):
    """출력 표기를 위한 헬퍼: float('inf') 는 'INF' 로 보여줌"""
    return [('INF' if x == INF else x) for x in dist]


if __name__ == "__main__":
    print("[테스트 1] 예시 그래프 (5개 정점)")
    n = 5
    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (2, 3, 5),
        (1, 3, 1),
        (3, 4, 3),
    ]
    print(f"  n={n}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 2] 정점 1개")
    print(f"  n=1, edges=[], start=0")
    print(f"  최단 거리: {_format(dijkstra(1, [], 0))}")
    print()

    print("[테스트 3] 도달 불가능한 정점 포함")
    n = 4
    edges = [(0, 1, 5)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 4] 동일한 거리의 두 경로 (둘 다 7)")
    n = 4
    edges = [(0, 1, 3), (1, 3, 4), (0, 2, 5), (2, 3, 2)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 5] 0 가중치 간선 포함")
    n = 3
    edges = [(0, 1, 0), (1, 2, 0), (0, 2, 5)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")