# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         result = ListNode(0)
# # Any Value to put head
#         result_tail = result
# # above result tail is meant to assign as a tailto result 
#         carry = 0
# #     carry is for carrying when number exceeds 9
                
#         while l1 or l2 or carry:  
#             val1 =(l1.val if l1 else 0)
           
            
# #             above cpde is to extract value stored from l1 list 
#             val2  = (l2.val if l2 else 0)
# #     similar for above code line 
# #       out = val1 + val2 +carry 
# #         carry =  out/10
#             carry, out = divmod(val1+val2 + carry, 10)  
    
# #     divmod return quotient and remainder 
                       
#             result_tail.next = ListNode(out)
#             result_tail = result_tail.next                      
# #             moing to the next node 
#             l1 = (l1.next if l1 else None)
#             l2 = (l2.next if l2 else None)
               
#         return result.next




# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):

#         # we initialize
#         dummy = current = ListNode()
#         carryover_value = 0


#         while l1 and l2:
#             d = carryover_value
#             if l1 and l2:
#                 d += (l1.val + l2.val)
#                 l1 = l1.next
#                 l2 = l2.next


            
#             elif l1:
#                 d += l1.val
#                 l1 = l1.next

#             elif l2:
#                 d += l2.val
#                 l2 = l2.next


#             # we calculate carryover

#             carryover_value = d//10

            
#             current.next = ListNode(d%10)
#             current = current.next
#         if carryover_value: current.next = ListNode(1)
# #             carryover never greater than 1
#         return dummy.next



# # complexity is 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        dummy = current = ListNode(0)
        #    create empty srting represent first numbers
        n1,n2 = "",""
        while l1:
            n1 = str(l1.val) +n1
            l1 = l1.next

        while l2:
            n2 = str(l2.val) + n2
            l2 = l2.next

        # we add n1 since we work backwards and we need to prepend
        if not n1: n1="0"
        if not n2: n2="0"

        sum = int(n1) + int(n2)
        
        for i in reversed(str(sum)):
            current.next = ListNode(int(i))
            current = current.next
        return dummy.next

    







