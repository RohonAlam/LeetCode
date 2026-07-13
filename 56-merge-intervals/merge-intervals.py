class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #First Implementation
        """
        intervals.sort(key = lambda x:x[0])
        results = [intervals[0]]

        for start,end in intervals[1:]:
            if start <= results[-1][1] :
                results[-1][1] = max(end,results[-1][1])
            else:
                results.append([start,end])
        return results
"""
        #Second Implementation
        intervals.sort(key = lambda x:x[0])

        results = []
        
        for interval in intervals :
            if not results or results[-1][1] < interval[0]:
                results.append(interval)
            else:
                results[-1][1] = max(interval[1],results[-1][1])
        return results