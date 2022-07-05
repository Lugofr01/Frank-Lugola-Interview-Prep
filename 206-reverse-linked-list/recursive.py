class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # recursive solution

        def recursive(previous, current):
            if not current:
                return previous
   
            tail = recursive(current, current.next)
            current.next = previous

            return tail
        return recursive(None,head)



time O{n} but space is O(n)
            


        
