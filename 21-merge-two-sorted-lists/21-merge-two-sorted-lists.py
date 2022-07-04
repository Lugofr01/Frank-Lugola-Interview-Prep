# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # we need linked list 
        # we travel down through linked list 
        # we move through the array and if it is a less value we add it to array 

        dummynode = output = ListNode()

        # dummynode will point to head and output will point to current


        while list1 and list2:
            # which cehck which is less to append to the output
            if list1.val <list2.val:
                # we add it to our toutput l1 is added since it is less 
                output.next = list1
                list1 =list1.next
            else:
                output.next = list2
                list2 = list2.next
                # we also move our pointer
            output = output.next

# we add the remainder of what emains to our output

        if list1: output.next =list1
#         else meeans if l2 reamais
        else: output.next = list2


        return dummynode.next
# o(n)  time complexity

# o(1) space 



