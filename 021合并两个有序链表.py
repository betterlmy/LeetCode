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


def mergeTwoLists(list1: [ListNode], list2: [ListNode]) -> [ListNode]:
    # 特殊值处理
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    new_list = ListNode()
    point = new_list

    while True:
        x = list1.val
        j = list2.val
        if x < j:
            new_list.val = x
            if list1.next is not None:
                list1 = list1.next
                new_list.next = ListNode()
                new_list = new_list.next
            else:
                new_list.next = list2
                break
        else:
            new_list.val = j
            if list2.next is not None:
                list2 = list2.next
                new_list.next = ListNode()
                new_list = new_list.next
            else:
                new_list.next = list1
                break
    return point


n1 = ListNode(1, next=ListNode(2, next=ListNode(4, None)))
n2 = ListNode(1, next=ListNode(3, next=ListNode(4, None)))

print(mergeTwoLists(n1, n2))
