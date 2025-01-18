# Given a singly linked list, determine if it contains a cycle
# A cycle occurs if a nodes next pointer references an earlier node in the LL, causing a loop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def does_ll_have_cycle(head: ListNode) -> bool:
        return false 
    
if __name__ == "__main__":
    solution = Solution()
    list1 = ListNode(2, ListNode(4, ListNode (6, None))) 
    list1ref = list1 
    while list1.next != None:
      list1 = list1.next

    list1.next = list1  #we are creating a loop back in the LL
    solution.does_ll_have_cycle(list1ref)
