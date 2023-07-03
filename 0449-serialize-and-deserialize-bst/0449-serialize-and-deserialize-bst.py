class Codec:
    def serialize(self, root):
        if not root:
            return ""
        res = []
        stack = [root]
        # preorder iterative traversal 
        while stack:
            cur_node = stack.pop()
            res.append(str(cur_node.val))
            res.append("/")
            if cur_node.right is not None:
                stack.append(cur_node.right)
            if cur_node.left is not None:
                stack.append(cur_node.left)
        return "".join(res[:-1])
            
    def deserialize(self, data):
        if not data:
            return None
        input_list = data.split("/")
        self.cur_index = 0
        def preorder(low, high):
            if self.cur_index == len(input_list):
                return None
            if not low <= int(input_list[self.cur_index]) < high:
                return None
            node = TreeNode(int(input_list[self.cur_index]))
            self.cur_index += 1
            node.left = preorder(low, node.val)
            node.right = preorder(node.val, high)
            return node
        return preorder(-inf, +inf)
            
            
            
            