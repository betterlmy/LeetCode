# author:TYUT-Lmy
# date:2021/12/22
# description:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        str1 = ''
        while self is not None:
            str1 += str(self.val)
            self = self.next
        return str1

def getlength(list1):
    index2 = 0
    while list1 is not None:
        index2 += 1
        list1 = list1.next
    return index2


def mergeTwoLists(list1: [ListNode], list2: [ListNode]) -> [ListNode]:
    # 特殊值处理
    if list1 is None:
        return list2
    elif list2 is None:
        return list1




n1 = ListNode(1, next=ListNode(2, next=ListNode(4, None)))
n2 = ListNode(1, next=ListNode(3, next=ListNode(4, None)))

print(n1)


