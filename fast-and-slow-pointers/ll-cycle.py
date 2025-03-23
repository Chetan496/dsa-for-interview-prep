# Given a singly linked list, determine if it contains a cycle
# A cycle occurs if a nodes next pointer references an earlier node in the LL, causing a loop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def does_ll_have_cycle(self, head: ListNode) -> bool:
        #both fast and slow pointers point to the head initially
        #you start iterating over the list 
        #slow pointer increments by one link
        #fast pointer by two links.
        # if at any point  - fast and slow point to same link, you exit the loop
        slow = head 
        fast = head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True
        return False 
    
if __name__ == "__main__":
    solution = Solution()
    node1 = ListNode(2, None)
    node2 = ListNode(4,None)
    node3 = ListNode(6, None)
    node1.next = node2 
    node2.next = node3 
    node3.next = node1 
    list1 = node1
    result = solution.does_ll_have_cycle(node1)
    print(result)
