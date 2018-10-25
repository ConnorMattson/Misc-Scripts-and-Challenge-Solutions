# Problem E - Team 19

dots = {'R': 0.55,'G': 0.70, 'B': 0.8, 'Y': 0.85, 'O': 0.9, 'W': 0.95}
purchases = int(input())

for i in range(purchases):
	item = input().split()
	price = float(item[0]) * dots[item[1]]
	
	if item[2] == 'C':
		price = price * 0.95
	
	priceList = []
	index = str(price).index('.')
	for i in str(price):
		if len(priceList) < index + 4:
			priceList.append(i)

	
	if int(priceList[-1]) > 4:
		priceList[-2] = str(int(priceList[-2]) + 1)
		priceList[-1] = '0'
	else:
		priceList[-1] = '0'
	
	del priceList[-1]
		
	if item[3] == 'C':
		if int(priceList[-1]) > 4:
			priceList[-2] = str(int(priceList[-2]) + 1)
			priceList[-1] = '0'
		else:
			priceList[-1] = '0'
	
	if str(priceList).index('.') == 0:
		priceList.insert(0, '0')
	
	
	while priceList[-3] != '.':
		priceList.append('0')
	
	print('$' + ''.join(priceList))
		
	
	