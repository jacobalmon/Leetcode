class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        n = len(nums)
        for i in range(n):
            hashMap[nums[i]] = i

        for i in range(n):
            comp = target - nums[i]
            if comp in hashMap and hashMap[comp] != i:
                return [i, hashMap[comp]]

        return []