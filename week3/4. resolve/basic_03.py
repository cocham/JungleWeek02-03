def create_graph(vertices, edges, directed=False):
    """
    그래프 생성 (인접 리스트)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
        directed: 방향 그래프 여부
    
    Returns:
        그래프 딕셔너리
    """
    
    graph = {}
    for i in range(vertices):
        graph[i] = []
    
    
    for edge in edges:
        start = edge[0]
        to = edge[1]
        
        graph[start].append(to)
        
        if (not directed):
            graph[to].append(start)

    
    return graph
        
    

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 무방향 그래프
    vertices = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    
    print("=== 무방향 그래프 ===")
    graph = create_graph(vertices, edges, directed=False)
    for vertex, neighbors in graph.items():
        print(f"{vertex} → {neighbors}")
    print()
    
    # 테스트 케이스 2: 방향 그래프
    print("=== 방향 그래프 ===")
    graph_directed = create_graph(vertices, edges, directed=True)
    for vertex, neighbors in graph_directed.items():
        print(f"{vertex} → {neighbors}")