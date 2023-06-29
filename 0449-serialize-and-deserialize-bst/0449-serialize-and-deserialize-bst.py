class Codec:
    def serialize(self, root):
        res = []
        def preorder(node):
            if not node:
                return 
            res.append(str(node.val))
            res.append("#")
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ''.join(res[:-1])
        
        
    def deserialize(self, data):
        if not data:
            return None
        input_list = list(map(int, data.split("#")))
        cur_index = 0
        def preorder(lower, upper):
            nonlocal cur_index
            if cur_index > len(input_list) - 1:
                return None
            if not lower <= input_list[cur_index] <= upper:
                return None
            
            val = input_list[cur_index]
            root = TreeNode(val)
            cur_index += 1
            
            root.left = preorder(lower, root.val)
            root.right = preorder(root.val, upper)
            
            return root
            
        return preorder(-inf, +inf)
            
            
            