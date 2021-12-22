# author:TYUT-Lmy
# date:2021/12/21
# description:
class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        hash = {}
        for i in nums:
            if i not in hash:
                hash[nums] = True
            else:
                return True
        return False
