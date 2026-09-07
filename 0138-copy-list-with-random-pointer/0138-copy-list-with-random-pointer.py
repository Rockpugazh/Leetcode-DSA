class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):

        if head is None:
            return None

        # Convert linked list into a list of nodes
        nodes = []

        current = head
        while current:
            nodes.append(current)
            current = current.next

        # Create new nodes using map()
        copies = list(map(lambda node: Node(node.val), nodes))

        # Create map: original node -> copied node
        old_to_new = dict(zip(nodes, copies))

        # Connect next and random
        for old in nodes:
            new = old_to_new[old]

            if old.next:
                new.next = old_to_new[old.next]

            if old.random:
                new.random = old_to_new[old.random]

        return copies[0]