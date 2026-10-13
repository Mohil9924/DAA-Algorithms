# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves using fast and slow pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None  # Disconnect the left half from the right half
        
        # Step 2: Recursively sort each half
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Step 3: Merge the two sorted halves
        return self.merge(left, right)
    
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Attach any remaining nodes
        tail.next = list1 if list1 else list2
        
        return dummy.next