class Solution(object):
    def runningSum(self, nums):
        new=[]
        running=0
        for i in nums:
            running+=i
            new.append(running)
        return new
sol=Solution()
result=sol.runningSum([1,2,3,4])
print(result)
        