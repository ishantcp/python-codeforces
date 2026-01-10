import sys

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index]) # Number of test cases
index += 1

results = []

for _ in range(t):
	n = int(data[index]) # Number of gas stations
	x = int(data[index + 1]) # Destination point
	index += 2

	# List to store points including start, gas stations, and destination
	points_list = [0]

	# Loop through each gas station
	for _ in range(n):
		point = int(data[index]) # Read each gas station point
		points_list.append(point) # Add gas station point to the list
		index += 1

	points_list.append(x) # Add destination point
	n = len(points_list) # Update n to include start, gas stations, and destination

	max_distance_between_points = -float('inf') # Variable to store the maximum distance between consecutive points

	# Loop through each point
	for i in range(1, n):
		if i == n - 1:
			# If it's the last point (destination), consider the round trip distance
			max_distance_between_points = max(max_distance_between_points, 2 * (points_list[i] - points_list[i - 1]))
		else:
			# Consider the one-way distance
			max_distance_between_points = max(max_distance_between_points, points_list[i] - points_list[i - 1])

	# Store the result for this test case
	results.append(max_distance_between_points)

# Output all results
for result in results:
	print(result)

# Time Complexity (TC): O(n) = O(50)
# Space Complexity (SC): O(n)