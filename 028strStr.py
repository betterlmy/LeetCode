class Solution:
    # 简单的滑块模式
    def exist(self, haystack, needle) -> int:
        for x in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[x + j] == needle[j]:
                    j += 1
                    if j == len(needle):
                        return x
                else:
                    break
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        # return self.exist(haystack, needle)
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


haystack = "hello"
needle = "a"
a = Solution()
print(a.strStr(haystack, needle))
