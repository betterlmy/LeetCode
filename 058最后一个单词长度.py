class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")
        length = len(x)
        x = x[::-1]
        for i in x:
            if i != "":
                return len(i)
        return 0
