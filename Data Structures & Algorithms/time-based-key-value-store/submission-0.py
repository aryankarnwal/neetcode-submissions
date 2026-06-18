class TimeMap:
   def __init__(self):
       self.hashmap = defaultdict(list)


   def set(self, key: str, value: str, timestamp: int) -> None:
       self.hashmap[key].append((timestamp, value))


   def get(self, key: str, timestamp: int) -> str:
       array = self.hashmap[key]
       if not array:
           return ""


       l = 0
       r = len(array) - 1


       while l <= r:
           m = (l+r)//2
           if array[m][0] == timestamp:
               return array[m][1]


           if array[m][0] < timestamp:
               l = m + 1
           else:
               r = m - 1
       if r >= 0:
           return array[r][1]
       return ""
