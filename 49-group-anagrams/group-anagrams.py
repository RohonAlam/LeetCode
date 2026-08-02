class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)

        for s in strs:
            groups["".join(sorted(s))].append(s)

        return list(groups.values())