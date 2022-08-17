


class Solution:
    def uniqueMorseRepresentations(self, words):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()

        for w in words:
            current = ''

            for c in w:
                index = alpha.index(c)
                current += morse[index]

            transformations.add(current)

        return len(transformations)
