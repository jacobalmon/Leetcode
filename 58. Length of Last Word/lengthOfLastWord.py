class Solution(object):
    def lengthOfLastWord(self, s):
        flag = False
        count = 0
        totalLength = len(s) - 1
        while totalLength >= 0:
            if s[totalLength] == ' ':
                if flag == True:
                    break
            else:
                flag = True
                count += 1
            totalLength -= 1
        return count   