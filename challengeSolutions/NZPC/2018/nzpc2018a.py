# Problem A 2018 - Connor Mattson

route = input("Enter the route name: ")
current = int(input("Enter the number of passengers initially on the bus: "))
maxPassengers = current
total = current

data = [int(x) for x in input("Enter the passengers getting on and leaving the bus, e.g. '4 2' enter '0 0' to exit: ").split(' ')]
while data != [0, 0]:
	total += data[0]
	current += data[0] - data[1]
	maxPassengers = max(maxPassengers, current)
	data = [int(x) for x in input("Enter the passengers getting on and leaving the bus, e.g. '4 2' enter '0 0' to exit: ").split(' ')]

print("Route {}\nTotal {}\nHighest {}".format(route, total, maxPassengers))