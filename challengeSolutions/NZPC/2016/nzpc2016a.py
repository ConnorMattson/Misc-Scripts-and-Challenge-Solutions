# Problem A 2016 - Connor Mattson

prices = []
for i in range(int(input("How many gifts are in the shop? "))): prices.append(float(input()))
print("The second cheapest gift costs ${:.2f}".format(sorted(prices)[1]))