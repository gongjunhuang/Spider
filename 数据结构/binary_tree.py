class Tree(object):
    """docstring fs Tree."""
    def __init__(self, element=None):
        self.left = None
        self.right = None
        self.element = element

    def traversal(self):
        """
        树的遍历, 是一个递归操作
        """
        print(self.element)
        if self.left is not None:
            self.left.traversal()
        if self.right is not None:
            self.right.traversal()

    def reverse(self):
        self.left, self.right = self.right, self.left
        if self.left is not None:
            self.left.reverse()
        if self.right is not None:
            self.right.reverse()

def test():
    t = Tree(0)
    left = Tree(1)
    right = Tree(2)
    t.left = left
    t.right = right
    t.traversal()

if __name__ == "__main__":
    test()
