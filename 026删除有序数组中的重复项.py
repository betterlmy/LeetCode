from typing import Union, Tuple, List


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        original_length = len(nums)
        length = original_length
        new_nums = nums
        i = 0
        while i < length:
            if i == length - 1:
                # 此时后面已经没有元素了
                break

            else:
                count = 0
                # 判断除自身外还有多少个连续的  类似于出现[1,2,2,2,2,2,2,...]的情况
                while True:
                    if i + count + 1 < length and new_nums[i] == new_nums[i + count + 1]:
                        count += 1
                    else:
                        break

                # 如果出现了相等 则需要删除后续 只保留一个,方法:让后续的所有元素(共original_length-count-i-1个元素)向前移动count个元素
                for x in range(1, length - count - i):
                    new_nums[i + x] = new_nums[i + x + count]

            length -= count
            i += 1

        return length, new_nums


original_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expected_list = [1, 2, 3, 4, 5, 5, 5]
s = Solution()
print(s.removeDuplicates(original_list))
pass
