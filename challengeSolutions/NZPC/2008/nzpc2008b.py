# Problem B 2008 - Connor Mattson

lineInput = input("Enter the number of tracks (0 to exit): ")
while lineInput != '0':
	
	songs = []
	print("Enter one song title per line...")
	for i in range(int(lineInput)):
		songs.append(input())

	print("---")
	songs.sort()
	for i in songs:
		print(i)

	lineInput = input("Enter the number of tracks (0 to exit): ")