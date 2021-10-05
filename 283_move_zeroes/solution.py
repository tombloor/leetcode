
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.moveZeroes_v1(nums)

    def moveZeroes_v1(self, nums: list[int]) -> None:
        length = len(nums)
        i = 0

        while i < length - 1:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                length = length - 1
            else:
                i = i + 1
