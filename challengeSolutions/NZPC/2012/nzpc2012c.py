#Problem C 2012 - Connor Mattson

data = [time.split(':') for time in input("Enter start time and duration, e.g. '03:50 06:10' or '00:00 00:00' to exit: ").split(' ')]
while data != [["00", "00"], ["00", "00"]]:
	minutes = int(data[0][1]) + int(data[1][1])
	hours = int(data[0][0]) + int(data[1][0]) + (minutes // 60)
	print("{0:0>2}:{1:0>2}".format(hours % 24, minutes % 60), "+{}".format(hours // 24)*(hours >= 24))
	data = [time.split(':') for time in input("Enter start time and duration, e.g. '03:50 06:10' or '00:00 00:00' to exit: ").split(' ')]