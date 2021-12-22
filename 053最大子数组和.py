class Solution:
    def maxSubArray(self, nums: list) -> int:
        add = 0
        first_big = -1
        max_num = 0
        for i in range(len(nums)):
            # 找到第一个大于0 的数
            if nums[i] > 0:
                add += nums[i]
                first_big = i
                max_num = add
                break

        if first_big == -1:
            # 找了一遍都没找到 直接返回最大的一个即可
            return max(nums)

        for i in range(first_big + 1, len(nums)):
            # 第二次遍历,寻找最大值
            add += nums[i]
            if add < 0:
                # 如果和已经小于0了 直接跳过比较
                add = 0
                continue
            max_num = add if add > max_num else max_num

        return max_num
a = Solution()
print(a.maxSubArray([1,-2,3]))