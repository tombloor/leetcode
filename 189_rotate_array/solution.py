import typing

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        self.rotate_v2(nums, k)

    def rotate_v2(self, nums: list[int], k: int) -> None:
        # Rotating is simply moving the last element to the front
        if len(nums) == 1:
            return

        k = k % len(nums)

        for rotation in range(0, k):
            last = nums.pop()
            nums.insert(0, last)

    def rotate_v1(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        # First lets prevent ourselves from doing unnecessary rotations
        k = k % len(nums)

        current_num = nums[0]
        prev_num = nums[0]

        for rotation in range(0, k):
            for i in range(0, len(nums)):
                prev_num = current_num
                current_num = nums[i]

                nums[i] = prev_num

                if i == len(nums) - 1:
                    nums[0] = current_num
