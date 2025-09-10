class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p,s in zip(position,speed):
            t = (target - p)/(s)
            cars.append((p,t))
        cars.sort(reverse = True, key=lambda x: x[0])
        stack = []
        for _,t in cars:
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack) 
