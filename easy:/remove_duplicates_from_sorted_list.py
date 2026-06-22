# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #set the current node to head
        cur = head
        #creat a while loop for the current and next node
        while cur and cur.next:
            #if the value of the current and the next nodes are the same
            if cur.val == cur.val.next:
                #move onto the next node
                cur.next = cur.next.next
            else:
                cur = cur.next
        #return the sorted linked list
        return head