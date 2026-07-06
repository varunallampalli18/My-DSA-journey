class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current=0
        highest=0
        for i in nums:
            if i==1:
                current+=1
            if current>highest:
                highest=current
            elif i==0:
                current=0
        return highest
sol=Solution()
result=sol.findMaxConsecutiveOnes([1,1,0,1,1,1])
print(result)
        