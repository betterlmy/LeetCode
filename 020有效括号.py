# author:TYUT-Lmy
# date:2021/12/22
# description:

dic1 = {
    '(': 0,
    '{': 0,
    '[': 0
}
dic2 = {
    ')': '(',
    '}': '{',
    ']': '['
}


def change(s):
    lens = len(s)
    s = s.replace('{}', '')
    s = s.replace('[]', '')
    s = s.replace('()', '')
    if lens > len(s):
        return True, s
    return False, s


def isValid(s: str) -> bool:
    changed = True
    while changed:
        if len(s) > 1:
            changed, s = change(s)
        else:
            changed = False
    return len(s) == 0


print(isValid("[()]"))
