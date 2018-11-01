# Problem D 2017 - Connor Mattson

data = list(input("Enter the musical sequence (letters A-G) e.g. 'ACE' or 'EBFA' enter '#' to exit: "))
while data != ['#']:
	for i in range(len(data)-1,0,-1): data[i] = ((ord(data[i]) - 65) - (ord(data[i - 1]) - 65)) % 7
	print("Ouch! That hurts my ears." if [x for x in data[1:] if x % 2 == 1] else "That music is beautiful.")
	data = list(input("Enter the musical sequence (letters A-G) e.g. 'ACE' or 'EBFA' enter '#' to exit: "))