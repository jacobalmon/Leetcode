class Solution(object):
    def addBinary(self, a, b):
        result = ""
        carry = 0

        max_length = max(len(a), len(b))
        a = a.zfill(max_length)
        b = b.zfill(max_length)

        for i in range(max_length - 1, -1, -1):
            total = carry

            total += 1 if a[i] == '1' else 0
            total += 1 if b[i] == '1' else 0
            carry = 1 if total > 1 else 0

            result = ('1' if total % 2 == 1 else '0') + result

        if carry != 0:
            result = '1' + result

        return result
        
