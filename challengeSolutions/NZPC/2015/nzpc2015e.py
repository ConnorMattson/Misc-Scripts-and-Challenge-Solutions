# Problem E - Team 19

dots = {'R': 0.55,'G': 0.70, 'B': 0.8, 'Y': 0.85, 'O': 0.9, 'W': 0.95}

for i in range(int(input("How many purchases are being made? "))):
	purchase = input("Enter purchase details: cost, discount dot (first letter of colour), coupon (C or X), and C for cash or P for plastic.\ne.g. '119.95 W C P': ").split()
	price = 0.00001 + float(purchase[0]) * dots[purchase[1]]
	if purchase[2] == 'C': price = price * 0.95
	
	price = list(str(price))
	if purchase[3] == 'C':
		if int(price[price.index('.') + 2]) > 5: price[price.index('.') + 1] = str(int(price[price.index('.') + 2]) + 1)
		price[price.index('.') + 2] = '0'

	print("This will cost: ${0:.2f}".format(float(''.join(price))))