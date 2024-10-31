class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ListNode(0)
        b = a
        c = 0

        while l1 is not None or l2 is not None or c != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + c
            digit = sum % 10
            c = sum // 10

            newNode = ListNode(digit)
            b.next = newNode
            b = b.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = a.next
        a.next = None
        return result
