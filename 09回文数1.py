# author:TYUT-Lmy
# date:2021/12/21
# description:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 转成str进行处理
        if x < 0:
            return False
        x = str(x)
        if x == x[::-1]:
            return True
        return False