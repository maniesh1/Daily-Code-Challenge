#Reverse a Linked List
# from pyparsing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr!=None:

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    

# Time Complexity: O(n)
# Space Complexity: O(1)

# Check for the test cases
reversed = Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print( reversed ,reversed.val)
