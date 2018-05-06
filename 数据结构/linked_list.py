class Node(object):
    def __init__(self, element=-1):
        self.element = element
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        index = 0
        node = self.head
        while node is not None:
            index += 1
            node = node.next
        return index

    def find(self, element):
        node = self.head
        while node is not None:
            if node.element == element:
                break
            node = node.next
        return node

    def _node_at_index(self, index):
        i = 0
        node =self.head
        while node is not None:
            if i == index:
                return node
            node = node.next
            i += 1
        return None

    def element_at_index(self, index):
        node = self._node_at_index(index)
        return node.element

    def insert_before_index(self, position):
        node = self._node_at_index(position)
        
        pass

    def insert_after_index(self, position):
        pass

    def first_object(self):
        pass

    def last_object(self):
        pass

    def append(self, node):
        if self.head is None:
            self.head.next = node
        else:
            last_node = self.last_object()
            last_node.next = next
            node.front = last_node
