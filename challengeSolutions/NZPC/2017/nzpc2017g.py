# Problem G 2017 - Connor Mattson

data = input("Enter the string to process: ").upper()
for i in range(65,91): print(chr(i) + " | " + "*"*data.count(chr(i)))