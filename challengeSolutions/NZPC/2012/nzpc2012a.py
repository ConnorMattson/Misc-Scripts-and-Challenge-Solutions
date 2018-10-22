#Problem A 2012 - Connor Mattson

year = int(input("Enter the year to check or '0' to exit: "))
while year != 0:
	print("{} was a leap year.".format(year) if year % 4 == 0 else "{} was a common year.".format(year))
	year = int(input("Enter the year to check or '0' to exit: "))