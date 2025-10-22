# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# Example 1:
# Input: head = [0,1,2,3]
# Output: [3,2,1,0]
# Example 2:
# Input: head = []
# Output: []

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head  
        while curr != None:      
            nextNode = curr.next   #nextNode points to 6 .. now nextNode points to 15
            curr.next = prev      #now curr.next points to None .. now curr.next ponts to head
            prev = curr     #prev points to head..now prev points to 6
            curr = nextNode  # curr points to 6 .. curr points to 15

        head = prev     
        return head
    
    def printLL(self, head: Optional[ListNode]):
        curr = head  
        while curr != None:      
            print(curr.val)
            curr = curr.next         
    
if __name__ == "__main__":
    solution = Solution()
    head = ListNode(5, ListNode(6, ListNode (1, None)))
    head2 = solution.reverseList(head)
    solution.printLL(head2)

            
        
