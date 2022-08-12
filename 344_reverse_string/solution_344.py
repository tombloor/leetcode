
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseString_v1(s)
        
    def reverseString_v1(self, s:list[str]) -> None:
        start = 0
        end = len(s) - 1

        while start < end:
            tmp = s[end]
            s[end] = s[start]
            s[start] = tmp
            start = start + 1
            end = end - 1