class Solution(object):
    def toLowerCase(self, s):
        return s.lower()
    
    def toLowerCase(self, s):
        newstring = ""
        for i in s:
            if 'A' <= i <= 'Z':
                newstring += chr(ord(i)+32)
            else:
                newstring += i
        return newstring