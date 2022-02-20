"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        length = len(nums)
        # 使用二分查找

        # 四个特殊情况
        if target <= nums[0]:
            return 0
        if target > nums[length - 1]:
            return length
        if length == 1:
            return 1

        min_index = 0
        max_index = length - 1
        while max_index > min_index:

            now_index = int((max_index + min_index) / 2)
            if nums[now_index] == target:
                # 如果正好找到了 -->直接输出
                return now_index
            elif nums[now_index] < target:
                # 二分移动指针
                min_index = now_index + 1
            else:
                max_index = now_index - 1

            if max_index == min_index:
                # max只会大于或者等于min  并不会相等 因为每次最多
                if nums[max_index] == target:
                    return max_index
                elif nums[max_index] > target:
                    if nums[max_index - 1] < target:
                        return max_index
                    elif nums[max_index - 1] == target:
                        return max_index - 1
                else:
                    if nums[max_index + 1] >= target:
                        return max_index + 1
            elif max_index < min_index:
                return max_index + 1

        return max_index


a = Solution()
print(a.searchInsert([3, 5, 7, 9, 10], 8))
