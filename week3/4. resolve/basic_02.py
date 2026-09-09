class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_bst(root, target):
    """
    BST에서 값 검색
    
    Args:
        root: 트리 루트
        target: 찾을 값
    
    Returns:
        True/False
    """
    if root is None:
        return False
    
    if (target == root.value):
        return True
    
    if (target < root.value):
        return search_bst(root.left, target)
        
    else:
        return search_bst(root.right, target)
        
    
    

# 테스트 케이스
if __name__ == "__main__":
    # BST 생성:
    #       5
    #      / \
    #     3   7
    #    / \
    #   2   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    
    print("=== 이진 검색 트리 ===")
    print("트리 구조: 5를 루트로 하는 BST")
    
    test_values = [2, 4, 5, 6, 7]
    for val in test_values:
        result = search_bst(root, val)
        print(f"값 {val} 검색: {result}")