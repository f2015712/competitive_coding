class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) in [0,1,2]:
            return len(nums)
        j=0
        for i in range(len(nums)):
            if i<len(nums)-2 and nums[i]==nums[i+2]:
                continue
            else:
                nums[j]=nums[i]
                j+=1
        return j