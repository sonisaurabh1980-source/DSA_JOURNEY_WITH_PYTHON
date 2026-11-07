"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        # Step 1: Insert cloned nodes immediately after original nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
            
        # Step 2: Assign random pointers for the cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # Step 3: Separate the interweaved list back into original and copied lists
        curr = head
        dummy = Node(0)
        copy_curr = dummy
        
        while curr:
            # Extract the copy
            copy_curr.next = curr.next
            copy_curr = copy_curr.next
            
            # Restore the original list structure
            curr.next = curr.next.next
            curr = curr.next
            
        return dummy.next


        