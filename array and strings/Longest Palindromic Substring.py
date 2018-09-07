class Solution(object):
    """
    def is_pal(string):
        if len(string) == 1:
            return True
        if len(string) == 2:
            return string[0] == string[1]
        if string[0] ==string[len(string)-1]:
        	return recursive(string[1:len(string)-1])
        else:
            return False
    
    def find(string, target):
        return [i for i, char in enumerate(string) if char == target]
    
    def combinations(list):
        result = []
        if len(list) == 0:
            return list
        for i in range(len(list)-1):
            for j in range(i+1:len(list)):
                result.append([list[i], list[j]])
        return result
    """
    def longestPalindrome(self, s):
        #CHECK FOR THE LONGEST ODD LENGTH PALINDROME INSIDE s
        longest = ""
        temp = ""
        for i in range(len(s)):
            temp = s[i]
            k = 1
            while i-k >= 0 and i+k < len(s):
                if s[i-k] == s[i+k]:
                    temp = s[i-k] + temp + s[i+k]
                    k += 1
                else:
                    k += len(s)
            if len(temp) > len(longest):
                longest = temp

        #CHECK FOR THE LONGEST EVEN LENGTH PALINDROME INSIDE s
        for i in range(len(s)-1):
            temp = ""
            k = 0
            while i-k >= 0 and i+1+k < len(s):
                if s[i-k] == s[i+1+k]:
                    temp = s[i-k] + temp + s[i+1+k]
                    k += 1
                else:
                    k += len(s)
            if len(temp) > len(longest):
                    longest = temp
        return longest
