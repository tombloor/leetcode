from collections import defaultdict

class Solution:
    def minSetSize(self, arr):
        # build a hashmap of counts O(n)
        counts = defaultdict(lambda: 0)
        for i in arr:
            counts[i] += 1

        # sort the values O(n log n)
        ordered_counts = sorted(counts.values())

        # pop largest counts until until cumulative count >= len(arr) // 2    O(n)
        target = len(arr) // 2
        cumulative = 0
        result = 0

        while cumulative < target:
            cumulative += ordered_counts.pop()
            result += 1

        return result # overall O(n log n)
