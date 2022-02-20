"""
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def removeElement(self, nums: list[int], val: int):

        length = len(nums)

        i = 0
        while i < length:
            count = 0
            if i == length:
                # 此时后面已经没有元素了
                break

            elif nums[i] == val:
                count = 1
                # 判断除自身外还有多少个连续的  类似于出现[1,2,2,2,2,2,2,...]的情况
                while True:
                    if i + count < length and nums[i] == nums[i + count]:
                        count += 1
                    else:
                        break

                # 如果出现了相等 则需要删除后续 只保留一个,方法:让后续的所有元素(共length-count-i-1个元素)向前移动count个元素
                for x in range(0, length - count - i):
                    nums[i + x] = nums[i + count + x]

            length -= count
            i += 1

        return length


a = Solution()
nums = [1, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(a.removeElement(nums, val))
