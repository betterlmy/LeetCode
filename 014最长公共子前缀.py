# author:TYUT-Lmy
# date:2021/12/21
# description:
def longestCommonPrefix(strs: list) -> str:
    # 找到最短的字符串
    shortest_str, shortest_lens = find_shortest(strs)
    while shortest_lens >= 0:
        flag = True
        for str1 in strs:
            a = shortest_str[:shortest_lens + 1]
            b = str1[:shortest_lens + 1]
            if a != b:
                shortest_lens -= 1
                flag = False
                break
        if flag:  return shortest_str[:shortest_lens + 1]
    return ""


def find_shortest(strs):
    index = 0
    shortest_lens = len(strs[0])
    for i in range(len(strs)):
        now_len = len(strs[i])
        if now_len < shortest_lens:
            index = i
            shortest_lens = now_len
    return strs[index], shortest_lens


print(longestCommonPrefix(["flower", "flow", "flight"]))
