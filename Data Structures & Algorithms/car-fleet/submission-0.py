class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #list comprehension

        #we're using key to read teh sorted list in descending order, sorted by default sorts lists in ascending order
        sorted_positions = sorted([(p,s) for p,s in zip(position, speed)], key = lambda t: -t[0])
        individual_time = [(target-p)/s for p,s in sorted_positions]
        
        #initialise our variables
        car_fleets = 0
        last_car_fleet_time = 0

        for time in individual_time:
            if time > last_car_fleet_time:
                #new fleet
                car_fleets += 1
                last_car_fleet_time = time
                #else we consider the car in the same fleet and the count remains same

        return car_fleets     