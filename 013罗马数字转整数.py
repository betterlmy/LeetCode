# author:TYUT-Lmy
# date:2021/12/21
# description:
dic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def romanToInt(s: str) -> int:

    sum = 0
    special = False
    for i in range(len(s)):
        if special:
            special = False
            continue
        now = s[i]
        a = dic[now]
        try:
            next = s[i+1]
        except IndexError:
            sum += a
            continue
        b = dic[next]
        if a < b:
            # 判断如果是特殊情况
            special = True
            sum += b
            sum -= a
        else:
            sum += a
    return sum
print(romanToInt('XIV'))