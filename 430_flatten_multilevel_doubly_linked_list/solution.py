
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

#Runtime: 36 ms, faster than 76.43% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
#Memory Usage: 14.5 MB, less than 94.01% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.

class Solution:
    # O(n)
    def flatten(self, head: Node) -> Node:
        # DFS to traverse the structure
        # At each iteration push next then child to stack
        # Pop from stack and repeat
        if head == None:
            return None

        stack = [head] 

        previous_node = None
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.next:
                stack.append(current_node.next)
            if current_node.child:
                stack.append(current_node.child)

            if previous_node:
                previous_node.next = current_node
                current_node.prev = previous_node

            current_node.child = None
            previous_node = current_node

        return head