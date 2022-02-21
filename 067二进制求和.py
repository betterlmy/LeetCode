def trans(list_a):
    x = ""
    for i in list_a:
        x += i
    return x


def addOne(new_a) -> str:
    # 实现+1操作
    list_a = list(new_a)
    for i in range(len(list_a)):
        if list_a[i] == "0":
            list_a[i] = "1"
            return trans(list_a)
        else:
            list_a[i] = "0"
    list_a.append("1")
    return trans(list_a)


def add(a, i):
    new_a = a[::-1]
    after_a = new_a[i:]
    before_a = new_a[:i]

    return (before_a + addOne(after_a))[::-1]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            tmp = a
            a = b
            b = tmp
        b = b[::-1]
        for i in range(len(b)):
            if b[i] == "1":
                a = add(a, i)

        return a