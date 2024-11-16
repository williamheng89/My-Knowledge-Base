'''
https://leetcode.com/problems/car-fleet/
'''
class Solution(object):
    '''
    Goal: Given a list of car positions and a correlating list of car speeds, find the number of car fleets that will be at the target position. In this problem, if a car is at a further position and is moving slower than a car at a smaller position, the fast car cannot pass the slow one and will become a fleet (driving at the slower car's speed)
    
    Plan:
    After hearing this problem, it appears that cars are limited the the slowest car ahead of them. Thus we should probably sort the cars in order based upon their positions because if the farthest car is moving super slow, any car behind them can catch up and just get stuck.
    
    So we know we should probably sort the cars
    
    In order to keep track of how many fleets of cars we will have, we essentially need to track the number of slowest cars of a group. In other wards, in every fleet, there is a "slowest" car such that it holds up everyone behind it.
    
    We can do so by sorting the car positions and then creating a stack. We then iterate decreasing from the farthest position to the shortest. We can compare the time it takes to reach the target : (target - position) / speed and add this to the stack. If stack[-1] <= stack [-2] meaning that the car behind the further car is traveling at a faster speed will catch up with the car in front before they reach the target, this will form a fleet and thus we pop that car. We keep contiuing and comparing and this mechanism will gurantee the grouping of fleets.
    '''
    def carFleet(self, target, position, speed):        
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """        
        car_fleet = [(p, s) for p, s in zip(position, speed)]
        car_fleet.sort(reverse=True)
        
        stack = []
        
        for p, s in car_fleet:
            stack.append((target - p) / float(s))
            if (len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)