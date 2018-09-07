class Solution(object):
    def lengthOfLongestSubstring(self, s):
        minDist = len(s)-1
        starts = []
        ends = []
        left = []
        right = []
        base = []
        longest = 0
        
        i = 0
        j = i+1
        if len(s) == len(set(s)):
            return len(s)
        for unique in set(s):
            temp = s.find(unique)
            while s.find(unique, temp+1) != -1:
                starts.append(temp)
                temp = s.find(unique, temp+1)
                ends.append(temp)
        for i in range(len(starts)):
            left.append(s[starts[i]:ends[i]])
            right.append(s[starts[i]:ends[i]])
            base.append(s[starts[i]:ends[i]])
        for i in range(len(starts)):
            left = right = base = s[starts[i]+1:ends[i]]
            if len(base) == len(set(base)):
                for l in s[:starts[i]+1][::-1]:
                    if l not in left:
                        left = l + left
                    else:
                        break
                for r in s[ends[i]:]:
                    if r not in right:
                        right = right + r
                    else:
                        break
                if longest < max(len(left), len(right)):
                    longest = max(len(left), len(right))
        return longest
