class Solution(object):
    def mostWordsFound(self, sentences):
        currentword=0
        maxword=0
        for i in sentences:
            count=0
            for j in i:
                if j==" ":
                    count+=1
                currentword=count+1
            if currentword>maxword:
                maxword=currentword
        return maxword
sol=Solution()
result=sol.mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"])
print(result)
                
        