class Solution(object):
    def isPalindrome(self, s):
        left = 0 # Left Pointer at the first index.
        right = len(s) - 1 # Right Pointer at the last index.
        
        # Loop until the pointer meet or past each other.
        while left < right:

            # Move Left Pointer until its a alphanumeric character.
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move Right Pointer until its a alphanumeric character.
            while left < right and not s[right].isalnum():
                right -= 1

            # Character are not the same, its not palindrome.
            if s[left].lower() != s[right].lower():
                return False

            left += 1 # Increment Left Pointer.
            right -= 1 # Increment Right Pointer.
        
        # If the string has been ran through completely, then its a palindrome.
        return True
