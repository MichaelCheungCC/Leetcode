# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        else:
            x=sorted([i for i in s])
            y=sorted([i for i in t])
            print(x)
            print(y)
            for i in range(len(s)):
                if x[i]!=y[i]:
                    return False
            return True