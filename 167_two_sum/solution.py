
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        return self.twoSum_v2(numbers, target)

    def twoSum_v2(self, numbers: list[int], target: int) -> list[int]:
        # List is ascending, therefore we can reduce the problem by converging inwards
        start = 0
        end = len(numbers) - 1

        # Scenario states there will always be exactly one solution, so this is fine
        while start < end:
            result = numbers[start] + numbers[end]
            if result == target:
                return [start + 1, end + 1]
            elif result < target:
                start = start + 1
            else:
                end = end - 1

    def twoSum_v1(self, numbers: list[int], target: int) -> list[int]:
        length = len(numbers)

        for i in range(0, length - 1):
            j = i + 1
            while j < length:
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                j = j + 1
