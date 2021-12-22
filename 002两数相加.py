# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return int2list(list2ine(l1) + list2ine(l2)).next


def list2ine(l: ListNode):
    sum = 0
    i = 1
    while l is not None:
        sum += (l.val * i)
        i *= 10
        l = l.next
    return sum


def int2list(sum: int):
    head = ListNode()
    p = head
    if sum == 0:
        temp = ListNode(0)
        p.next = temp

    while sum > 0:
        a = sum % 10
        sum = sum // 10
        temp = ListNode()
        temp.val = int(a)
        p.next = temp
        p = temp
    return head


def get_ListNode(li):
    head = ListNode()
    p = head
    for i in li:
        temp = ListNode()
        temp.val = i
        p.next = temp
        p = temp
    return head


if __name__ == '__main__':
    l1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    l2 = [5, 4, 3]
    l1 = get_ListNode(l1)
    l2 = get_ListNode(l2)
    s = Solution()
    list = s.addTwoNumbers(l1.next, l2.next)
    while list is not None:
        print(list.val, end="")
        list = list.next
