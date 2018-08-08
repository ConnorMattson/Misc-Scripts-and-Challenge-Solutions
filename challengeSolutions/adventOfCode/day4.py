import hashlib

a = 'abcdef609043'.encode('UTF-8')

md5hash = '11111111111'




code = 'iwrupvqb'
number = 0


# For finding first 5 x 0
# while str(md5hash[0:5]) != '00000':
# 	number += 1
# 	a = code + str(number)
# 	a = a.encode('UTF-8')

# 	md5hash = hashlib.md5()
# 	md5hash.update(a)
# 	md5hash = md5hash.hexdigest()

# print(number)


#  For finding first 6 x 0
while str(md5hash[0:6]) != '000000':
	number += 1
	a = code + str(number)
	a = a.encode('UTF-8')

	md5hash = hashlib.md5()
	md5hash.update(a)
	md5hash = md5hash.hexdigest()

print(number)