from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        bucket = defaultdict(list)
        res = []

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for key, v in count.items():
            bucket[v].append(key)
        
        ordered = sorted(bucket.items(), reverse=True)
        
        for key,v in ordered:
            while len(res) < k and v:
                res.append(v.pop())
            if len(res) == k:
                return res
        return res