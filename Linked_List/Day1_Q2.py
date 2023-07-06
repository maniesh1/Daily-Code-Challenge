#Find the middle of the linked list

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# brute force approach is to find the length of the linked list and then find the middle element.
# time compexity: O(n)
# space complexity: O(1)
class Solution:
    def middle_node(self, head : ListNode):
        if head is None:
            return []
        curr = head

        count = 1
        while curr!=None:
            curr = curr.next
            count += 1

        curr = head
        for i in range(count//2-1 if count%2==0 else count//2):

            curr = curr.next
        return curr

# test the code
linked_list = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
print(Solution().middle_node(linked_list).val)

# optimal approach is to use two pointers, one slow and one fast.
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def middle_node2(self, head : ListNode):
        slow, fast = head, head
        
        while fast !=None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next
        return slow
    

linked_list = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
print(Solution().middle_node2(linked_list).val)

