class Solution(object):
    def containsDuplicate(self, nums):
        dub=set()
        for i in nums:
            if i in dub:
                return True
            dub.add(i)
        return False 



        