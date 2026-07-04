import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x,y):
            return (x**2 + y**2)**(0.5)
        heap = []
        heapq.heapify(heap)

        for i,v in enumerate(points):

            dist = distance(v[0],v[1])
            heapq.heappush(heap, (dist,i))
        
        res = []

        for i in range(k):
            index = heapq.heappop(heap)[1]
            res.append(points[index])
        
        return res

