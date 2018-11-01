# Problem B 2018 - Connor Mattson

import math

toys = []
for i in range(int(input("How many toys do you wish to sort? "))): toys.append(input("Enter toy {}: ".format(i + 1)))

toys = sorted(toys)
for j in range(math.ceil(len(toys) / 2)): print(toys[j] + ', ' + toys[-(j + 1)] if j + 1 <= len(toys) // 2 else toys[j])