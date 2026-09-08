# 스택을 이용한 DFS

def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (스택)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    visited = [False] * len(graph)
    result = []
    stack = [start]

    while stack:
        node = stack.pop()
        
        if (visited[node]):
            continue
        
        visited[node] = True
        result.append(node)
        
        for next in graph[node]:
            if not visited[next]:
                stack.append(next)
                
                
    return result


# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

