class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        for i in nums:
            ans.append(i)
        for i in nums:
            ans.append(i)
        return ans
sol=Solution()
result=sol.getConcatenation([1,2,1])
print(result)