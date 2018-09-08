import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        tasks_counter = collections.Counter(tasks)
        most_common = tasks_counter.most_common(1)[0][1] #the frequency of the most frequent task
        numMost = 0
        while numMost < len(set(tasks)):
            if tasks_counter.most_common(numMost+1)[numMost][1] == most_common:
                numMost += 1
            else:
                break
        return max(((most_common-1) * (n+1) + numMost), len(tasks))
