class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
    
        reference = strs[0]
        prefix_length = len(reference)
        
        for i in range(prefix_length):
            char = reference[i]
            for other in strs:
                if i >= len(other) or other[i] != char:
                    return reference[:i]
        
        return reference
        
