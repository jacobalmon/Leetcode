class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = left = 0
        index_map = {}

        for right in range(len(s)):
            if s[right] in index_map and index_map[s[right]] >= left:
                left = index_map[s[right]] + 1
            
            index_map[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
        
