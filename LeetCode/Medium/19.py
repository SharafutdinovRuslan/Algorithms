# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        remove_node = head
        current_node = head
        prev_node = None

        for _ in range(n):
            current_node = current_node.next

        while current_node:
            current_node = current_node.next
            prev_node = remove_node
            remove_node = remove_node.next

        if not prev_node:
            return head.next

        prev_node.next = remove_node.next

        return head


if __name__ == "__main__":
    a = Solution().removeNthFromEnd(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
    )

    a = Solution().removeNthFromEnd(
        ListNode(1), 1
    )

    a = (Solution().removeNthFromEnd(
        ListNode(1, ListNode(2)), 2)
    )
