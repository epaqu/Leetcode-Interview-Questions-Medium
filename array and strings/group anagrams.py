from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anas = defaultdict(list)
        for s in strs:
            counts = [0]*26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            anas[tuple(counts)].append(s)
        return anas.values()
