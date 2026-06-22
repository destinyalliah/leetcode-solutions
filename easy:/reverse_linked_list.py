# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #set the current node to head
        cur = head
        #set the previous node to None
        prev = None

        #create a while loop for the current node
        while cur:
            #hold the actual cur.next value
            temp = cur.next
            #reverse list
            cur.next = prev
            #set the previous value to the current value
            prev = cur
            #move the current value to cur.next
            cur = temp
        
        return prev