class Solution(object):
    def getlength(self,start,end,s):
        while start<=end and start>=0 and  end<len(s) and s[start]==s[end]:
            start-=1
            end+=1
        return [start,end]
    def longestPalindrome(self, s):
        start=0
        end=0
        if len(s)==0 or len(s)==1:
            return s
        if len(s)==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        # for each index, move to the left and right and check pallindrome

        for i in range(len(s)):
            #for odd length pallindrome
            startlen1,endlen1=self.getlength(i,i,s)
            #for even length pallindrome
            startlen2,endlen2=self.getlength(i,i+1,s)
            length=max(endlen1-startlen1,endlen2-startlen2)
            if length>end-start:
                if length==endlen1-startlen1:
                    end,start=endlen1,startlen1
                else:
                    end,start=endlen2,startlen2
        return s[start+1:end]