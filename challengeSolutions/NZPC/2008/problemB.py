# Problem B - Connor Mattson

lineInput = input()
while lineInput != '0':
	songs = []
	for i in range(int(lineInput)):
		track = input()
		songs.append(track)

	songs.sort()
	for i in songs:
		print(i)

	lineInput = input()