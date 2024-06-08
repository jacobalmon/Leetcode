class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        # Ensure text1 is the longer string.
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        prev = [0] * (len(text2) + 1) # List for previous iteration.
        curr = [0] * (len(text2) + 1) # List for current iteration.

        # Traverse the two strings from the end to start.
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # If characters match, then increase LCS by 1.
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                # Otherwise take the maximum length possible.
                else:
                    curr[j] = max(prev[j], curr[j + 1])

            # Swap the lists.
            prev, curr = curr, prev

        # The length of the LCS is stored at this position.
        return prev[0]
