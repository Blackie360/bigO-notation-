def min_refueling_stops(D, max_distance):
    n = len(D)
    refueling_stops = 0  # Number of refueling stops made
    current_position = 0  # Current position

    # Iterate until the destination is reached
    while current_position < n - 1:
        farthest_station = current_position

        # Find the farthest reachable fuel station from the current position
        while (farthest_station < n - 1) and (D[farthest_station + 1] - D[current_position] <= max_distance):
            farthest_station += 1

        # If the farthest station is the same as the current position, it's not possible to reach the destination
        if farthest_station == current_position:
            return float('inf')

        # Update the current position to the farthest station reached
        current_position = farthest_station

        # Increment the number of refueling stops made
        refueling_stops += 1

    return refueling_stops

# Example usage
D = [0, 50, 100, 180, 210, 250, 300]  # Distance of fuel stations from the start
max_distance = 200  # Maximum distance the vehicle can travel before refueling

result = min_refueling_stops(D, max_distance)
if result == float('inf'):
    print("It is not possible to reach the destination.")
else:
    print(f"The least number of refueling stops required: {result}")
