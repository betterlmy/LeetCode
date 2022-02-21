from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        for i in range(len(digits) + 1):
            try:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits[::-1]
            except IndexError:
                digits.append(1)
                return digits[::-1]
