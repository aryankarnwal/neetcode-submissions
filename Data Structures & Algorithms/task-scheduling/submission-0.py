import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]

        heapq.heapify(maxheap)

        q = deque()

        while maxheap or q:
            time += 1

            if maxheap:
                cnt = heapq.heappop(maxheap) + 1
                if cnt:
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        
        return time

