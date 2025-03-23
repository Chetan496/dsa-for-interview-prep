# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
# The new list should be made up of nodes from list1 and list2.
# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1 
        head2 = list2 
        head3 = ListNode(0,None)
        head3initial = head3 
        while head1.next != None and head2.next != None:
            if head1.val <= head2.val:
                head3.val = head1.val
                print("copied from list1")
                head1 = head1.next 
                head3.next = ListNode(0, None)
                head3 = head3.next
            if head2.val < head1.val:
                head3.val = head2.val 
                print("copied from list2")
                head2 = head2.next
                head3.next = ListNode(0, None)
                head3 = head3.next

        if head1.next == None:
            while head2 != None: 
                head3.val = head2.val
                print("copied from list2")
                head3.next = ListNode(0,None)
                head3 = head3.next
                head2 = head2.next                

        if head2 == None:
            while head1 != None: 
                head3.val = head1.val
                print("copied from list1")
                head3.next = ListNode(0,None)
                head3 = head3.next
                head1 = head1.next                 

        # if head1 != None 

        return head3initial
    
    
    def printLL(self, head: Optional[ListNode]):
        curr = head  
        while curr != None:      
            print(curr.val)
            curr = curr.next             
    
if __name__ == "__main__":
    solution = Solution()
    list1 = ListNode(2, ListNode(4, ListNode (6, None)))
    list2 = ListNode(1, ListNode(3, ListNode (5, ListNode(6, None))))
    list3 = solution.mergeTwoLists(list1,list2)
    solution.printLL(list3)

        