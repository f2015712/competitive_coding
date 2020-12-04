class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start=0
        n=len(s)
        if n==0 or n==1:
            return n
        max_len=-10000000
        
        while start<n:
            #print(start)
            count=0
            visited={}
            for i in range(start,n):
                if s[i] not in visited:
                    count+=1
                    visited[s[i]]=1
                    max_len=max(max_len,count)
                else:
                    max_len=max(max_len,count)
                    
                    break
            start+=1
        return max_len