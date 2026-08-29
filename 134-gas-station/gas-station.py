class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        gain  = 0
        n = len(gas)
        start = 0
        for i in range(n):
            gain = gas[i]  - cost[i]
            tank += gain
            total += gain

            if tank < 0 :
                start = i + 1
                tank = 0
        if total >= 0 :
            return start
        else:
            return -1


           
        