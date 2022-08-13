

class Solution:
    def findSubstring(self, s, words):
        # n = len(words[0])
        # Sliding window of n * len(words) as all words are the same length
        # Keep a hashmap that has counts of words looking for
            # Decrement when found, if we get to -1 then reset and move start forward 1 char
            
        n = len(words[0])
        result = []
        
        missing = {}
        start = 0
        end = start + (n * len(words))
        
        # Setup the search dictionary
        for w in words:
            missing[w] = missing.get(w, 0) + 1
        
        while end <= len(s):
            m = missing.copy()
            
            for i in range(0, len(words)):
                tmp_start = start + (i * n)
                a = s[tmp_start:tmp_start + n]
                if a in m:
                    m[a] -= 1
                    if m[a] < 0:
                        break
                else:
                    break
                
            if sum(m.values()) == 0 and min(m.values()) == 0:
                result.append(start)
            
            start += 1
            end += 1
        
        return result