class Solution(object):
    def isAnagram(self, s, t):
        # if the string sizes are not the same, then they can't be permutations.
        if len(s) != len(t):
            return False
        
        # initializing list to all 0 to keep track of each occurance.
        letters = [0] * 26

        # incrementing each character according to their ASCII code for s.
        for char in s:
            letters[ord(char) - ord('a')] += 1

        # decrementing each character according to their ASCII code for string t.
        for char in t:
            letters[ord(char) - ord('a')] -= 1
            # when decrementing if it ever becomes less than 0, then it's not a permutation.
            if letters[ord(char) - ord('a')] < 0:
                return False

        return True
        
