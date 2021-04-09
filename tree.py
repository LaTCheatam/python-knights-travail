class Node:
    def __init__(self, value):
        '''
        Construct a new Node class and initialize.
        '''
        self._value = value
        self._parent = None
        self._children = []
        

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if not node in self._children:
            self._children.append(node)
            node.parent = self   # = node.parent(self)   >> we are setting the parent (setter)

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)   
            node.parent = None   # = node.parent(None) becareful do not write node._parent = None we don't want to access another node 

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent is node:
            return
        if self._parent:
            self._parent.remove_child(self)
        self._parent = node
        if node is not None:
            node.add_child(self)

    def depth_search(self, value):
        if self._value == value:
            return self
        for child in self._children:
            node = child.depth_search(value)
            if node is not None:
                return node

    def breadth_first(self, value):
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return node
            queue.extend(node._children)




node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)