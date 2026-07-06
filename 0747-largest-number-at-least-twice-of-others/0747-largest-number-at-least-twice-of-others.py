class Solution(object):
    def dominantIndex(self, nums):
        largest=float('-inf')
        indexlarg=0
        for i in range(len(nums)):
            if nums[i]>largest:
                largest=nums[i]
                indexlarg=i
        for i in range(len(nums)):
            if i==indexlarg:
                continue
            if largest<2*nums[i]:
                return -1
        return indexlarg
sol=Solution()
result=sol.dominantIndex([3,6,1,0])
print(result)