class Solution(object):
    def findNumbers(self, nums):
        
        evencount=0
        for i in nums:
            count=0
            while i>0:
                digit=i%10
                count+=1
                i=i//10
            if count%2==0:
                evencount+=1
        return evencount
sol=Solution()
result=sol.findNumbers([12,345,2,6,7896])
print(result)
                
        