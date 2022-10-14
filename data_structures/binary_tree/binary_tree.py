# Binary Tree

class Node(object):
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._left_child = None
        self._right_child = None
        self.flag = False
        
    @property
    def value(self):
        return self._value
        
    @value.setter
    def value(self, val):
        self._value = val
        
    @property
    def parent(self):
        return self._parent
        
    @parent.setter
    def parent(self, val):
        self._parent = val
    
    @property
    def left_child(self):
        return self._left_child
        
    @left_child.setter
    def left_child(self, val):
        self._left_child = val
        
    @property
    def right_child(self):
        return self._right_child
        
    @right_child.setter
    def right_child(self, val):
        self._right_child = val
        

class BinaryTree(object):
    def __init__(self):
        self._root = None
        self._current = self._root
        
    def set_root(self, value):
        root = Node(value)
        self._root = root
        self._current = self._root
        
    def set_left(self, value):
        left_node = Node(value)
        left_node.parent = self._current
        self._current.left_child = left_node
        return left_node
        
    def set_right(self, value):
        right_node = Node(value)
        right_node.parent = self._current
        self._current.right_child = right_node
        return right_node
        
    def reset_current(self):
        self._current = self._root
        return self._root
        
    def bfs(self):
        stack = []
        stack.append(self._root)
        while len(stack)>0:
            node = stack.pop()
            print(node.value)
            if not node.flag:
                if node.left_child != None:
                    stack.append(node.left_child)
                if node.right_child != None:
                    stack.append(node.right_child)
                node.flag = True


if __name__ == '__main__':
    tree = BinaryTree()
    tree.set_root(1)
    tree.set_right(2)
    tree.set_left(3)
    tree.set_left(4)
    print('BFS')
    tree.bfs()


