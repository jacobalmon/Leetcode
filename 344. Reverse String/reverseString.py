class Solution(object):
    def reverseString(self, s):
        end = len(s) - 1
        for start in range(len(s)):
            if start >= end:
                break
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            end -= 1
        return s