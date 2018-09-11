# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def join(self, interval1, interval2):
        if interval1.end < interval2.end:
            interval1.end = interval2.end
        return interval1
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key = lambda interval : interval.start)
        merged = [intervals[0]]
        i = 1
            #for [a, b] and [c, d]
        while i < len(intervals):
            #case 1 a < c < b&d
            if intervals[i-1].start <= intervals[i].start <= intervals[i-1].end:
                if intervals[i-1].end < intervals[i].end:
                    intervals[i-1].end = intervals[i].end
                del intervals[i]
            elif intervals[i].start <= intervals[i-1].start <= intervals[i].end:
                if intervals[i].end < intervals[i-1].end:
                    intervals[i].end = intervals[i-1].end
                del intervals[i-1]
            else:
                i += 1

        return intervals
