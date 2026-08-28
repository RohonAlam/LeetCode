from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        q = deque()

        for i, ticket in enumerate(tickets):
            q.append((ticket, i))

        while q:
            remaining, index = q.popleft()

            # Person buys one ticket
            remaining -= 1
            time += 1

            # Person k has bought all required tickets
            if index == k and remaining == 0:
                return time

            # Put the person back if they still need tickets
            if remaining > 0:
                q.append((remaining, index))

        return time