import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new = []
        for stone in stones:
            heapq.heappush(new, stone*-1)

        while len(new) > 1:
            stone1 = heapq.heappop(new)*-1
            stone2 = heapq.heappop(new)*-1
            stone3 = 0 

            if stone1 > stone2:
                stone3 = stone1 - stone2
            
            if stone3 > 0:
                heapq.heappush(new, stone3*-1)
        
        if new:
            return new[-1]*-1
        return 0 
        