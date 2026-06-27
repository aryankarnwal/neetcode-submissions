import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

        if nums:
            heapq.heapify(self.heap)
        while self.heap and len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if self.heap and len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
