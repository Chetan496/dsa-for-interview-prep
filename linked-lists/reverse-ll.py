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
        curr = head  
        while curr.next != None:      
            print(curr.val)
            curr = curr.next 
        return None 
    
if __name__ == "__main__":
    solution = Solution()
    head = ListNode(4, ListNode(6, ListNode (1, None)))
    solution.reverseList(head)

            
        
