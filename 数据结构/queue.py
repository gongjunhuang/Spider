"""

队列的特点是「先进先出」，一般有这几个操作

# enqueue 将一个元素存入队列中
# dequeue 将一个元素从队列中取出，并在队列中删除它

# empty 查看栈是否是空的


可以把队列看做排队，银行叫号机就是队列，先取号的先入队，叫号的时候也就先出队

"""
# Node类是一个节点，有两个属性，一个存储元素，一个存储指向另一个节点的引用
class Node():
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __repr__(self):
        return str(self.element)

    def empty(self):
        return self.head.next is None

    def enqueue(self, element):
        n = Node(element)
        self.tail.next = n
        self.tail = n

    def dequeue(self):
        node = self.head.next
        if not self.empty():
            self.head.next = node.next
        return node
        
