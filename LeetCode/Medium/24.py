# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        output = head

        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next

        return output


if __name__ == "__main__":
    a = Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    # a = Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3))))
    # a = Solution().swapPairs(ListNode())
    print("asdfa")
