# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        # nth node is the one at n and linked list start from the back



        # we need a Dummy node and fast and slow pointer


        dummynode = fast = slow = ListNode(0,next=head)
        # will help us return head of linked list and dummy poiter helps us know where the headis iat


        # let's move our fast ponter n steps

        for _ in range(n):
            fast =fast.next
            # we move  both pointers

        while fast.next:
            # we move our fast and slow
            fast = fast.next
            slow = slow.next


            # slow pointer will point righ before the node we want to remove
            # we move both pointers upto fast doesnt point to anythng

        # to update our slow.next we add another next

        slow.next = slow.next.next
        # if next.next doesnt exist we point to a none

        return dummynode.next


         

        
        
        