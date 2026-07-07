class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        larg=float('-inf')
        for i in candies:
            if i>larg:
                larg=i
        result=[]
        stored=0
        for i in range(0,len(candies)):
            stored=candies[i]+extraCandies
            if stored>=larg:
                result.append(True)
            else:
                result.append(False)
        return result
sol=Solution()
result=sol.kidsWithCandies([2,3,5,1,3],3)
print(result)
        