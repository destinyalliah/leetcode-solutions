class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # step 1: find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # step 2: reverse second half
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # step 3: merge
        first, second = head, prev
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next