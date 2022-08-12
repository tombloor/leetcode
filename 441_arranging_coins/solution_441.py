class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 0
        while n >= 0:
            n -= row
            if n >= row + 1:
                row += 1
            else:
                break
        return row
