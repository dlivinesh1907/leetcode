class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.children:
                for child in reversed(node.children):
                    if child:
                        stack.append(child)
                        
        return result