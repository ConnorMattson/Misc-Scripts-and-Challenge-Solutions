#Problem C - Connor Mattson

# We are given a start time and the duration of the event
# When does the event end?




# Split into initial and final
# Split the input into hours and minutes

# Add the minutes, is it more than 60?
# add the hours, more than 24?

# if > 24, remove 24 hours
# add +1 days

#h1 is hours of first time

#m1 is minites of first time
#h2 is hours of second time
#m2 is minites of second time
#ht is the total hours
#mt is the total minutes

sample_input = "03:50 06:10"

def add_times(h1, m1, h2, m2):
	mt = m1 + m2
	ht = h1 + h2
	while mt >= 60:
		ht += 1
		mt -= 60
	return[ht, mt]

timein = sample_input #put it raw time here

x = list(timein)
h1 = int(x[0] + x[1])
m1 = int(x[3] + x[4])
h2 = int(x[6] + x[7])
m2 = int(x[9] + x[10])

finalTime = add_times(h1, m1, h2, m2)
hours = finalTime[0]
minutes = finalTime[1]

standard = 24
days = 0
while hours > standard:
	standard = standard + 24
	days = days + 1

if days == 0:
	print("{}:{}".format(hours, minutes))
else:
	print("{}:{} +{}".format(hours, minutes, days))
	
#returns 10:0