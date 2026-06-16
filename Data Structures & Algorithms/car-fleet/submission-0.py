class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars, reverse=True)
        stack = []


        for i in range(len(cars)):
            time = (target - cars[i][0])/cars[i][1]


            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)




        return len(stack)
