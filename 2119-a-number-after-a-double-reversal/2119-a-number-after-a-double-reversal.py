class Solution(object):
    def isSameAfterReversals(self, num):
        original=num
        rev=0
        rev1=0
        while num>0:
            digit=num%10
            rev=rev*10+digit
            num=num//10
        while rev>0:
            digit1=rev%10
            rev1=rev1*10+digit1
            rev=rev//10
        if original==rev1:
            return True
        else:
            return False
sol=Solution()
result=sol.isSameAfterReversals(526)
print(result)

        