# Def# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # let's start iteratively
        # we have two pointers pointing to previous node and current node
        # we want to reverse the ponters

        previous = None
        current = head

        while current:
            # reversing the pointers
            temporarystorage = current.next
            # we store the current nodes temporry

            current.next = previous
            # we point to  previous node

            previous = current
            current = temporarystorage


        return previous
    
    
# o(n)  time complexity, memory O(1)

# class ListNode:

#     def __init__(self, val=0, next=None):

#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         # recursive solution

#         def recursive(previous, current):
#             if not current:
#                 return previous

#             tail = recursive(current, current.next)
#             current.next = previous

#             return tail
#         return recursive(None,head)



# time O{n} but space is O(n)
            


        