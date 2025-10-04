class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are different
        if len(s) != len(t):
            return False

        countS , countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)  # if s[i] in countS, increment its count, else initialize to 1
            countT[t[i]] = 1 + countT.get(t[i],0)

        # Iterate through countS and compare with countT
        for c in countS: 
            if countS[c] != countT.get(c, 0): 
                return False

        return True