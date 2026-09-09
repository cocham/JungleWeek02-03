class TreeNode:
    """이진 트리 노드"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    """전위 순회: 루트 → 왼쪽 → 오른쪽"""
    if root is None:
        return []
    
    return [root.value] + preorder(root.left) + preorder(root.right)
    

def inorder(root):
    """중위 순회: 왼쪽 → 루트 → 오른쪽"""
    
    if root is None:
        return []
    
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    """후위 순회: 왼쪽 → 오른쪽 → 루트"""
    if root is None:
        return []
    
    return postorder(root.left) + postorder(root.right) + [root.value]

    

# 테스트 케이스
if __name__ == "__main__":
    # 트리 생성:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("=== 이진 트리 순회 ===")
    print(f"전위 순회: {preorder(root)}")
    print(f"중위 순회: {inorder(root)}")
    print(f"후위 순회: {postorder(root)}")