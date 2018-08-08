# Problem J - Team 19

def upper (start_idx, end_idx, str_in):
	pro_in = str_in[start_idx + 1 : end_idx]
	pro_out = pro_in.upper()
	
	return(str_in[0: start_idx] + pro_out + str_in[end_idx + 1 : len(str_in)])

def double_quotes (start_idx, end_idx, str_in):
	pro_in = str_in[start_idx + 1 : end_idx]
	pro_out = ''
	for i in pro_in:
		if i == '\"':
			pro_out += '\\"'
		else:
			pro_out += i
	
	return(str_in[0: start_idx] + pro_out + str_in[end_idx + 1 : len(str_in)])
	
def reversal (start_idx, end_idx, str_in):
	pro_in = str_in[start_idx + 1 : end_idx]
	pro_list = list(pro_in)
	pro_list.reverse()
	pro_out = ''
	for i in pro_list:
		pro_out += i
	
	return(str_in[0: start_idx] + pro_out + str_in[end_idx + 1 : len(str_in)])
	
def hex_me (start_idx, end_idx, str_in):
	pro_in = str_in[start_idx + 1 : end_idx]
	pro_list = pro_in.split(' ')
	pro_out = ''
	print(pro_list)
	for i in range(len(pro_list)):
		try:
			print('yes')
			temp = list(str(hex(int(pro_list[i]))))
			print(type(temp))
			del temp[0]
			del temp[0]
			
			pro_out += (''.join(temp)) + ' '
			print(temp)
		except:
			pro_out += pro_list[i] + ' '

	
	#for i in pro_list:
		#pro_out += i + ' '
	
	
	return(str_in[0: start_idx] + pro_out[0: len(pro_out) - 1] + str_in[end_idx + 1 : len(str_in)])

print(hex_me(0, 23, '#text with 31 12 and 64#'))
raw_line = input()
while cur_line != '#':
	cur_line = raw_line
	finished = False
	while finished == False:
		mark_ops = []
		mark_pos = []
		ignored = False
		for i in cur_line:
			if cur_line[i] == '@':
				if ignored == False:
					ignored = True
				elif ignored == True:
					ignored = False
			elif ignored == False and cur_line[i] in '^\#<':
				mark_ops.append(cur_line[i])
				mark_pos.append(i)
		
		if len(mark_ops) == 0:
			finished = True
		else:
			for i in range(len(mark_ops)-1):
				if mark_ops[i] == mark_ops[i + 1]:
					if mark_ops[i] == '^':
						cur_line = upper(mark_pos[i], mark_pos[i + 1], cur_line)
					elif mark_ops[i] == '\'':
						cur_line = double_quotes(mark_pos[i], mark_pos[i + 1], cur_line)
					elif mark_ops[i] == '<':
						cur_line = reversal(mark_pos[i], mark_pos[i + 1], cur_line)
					elif mark_ops[i] == '#':
						cur_line = hex_me(mark_pos[i], mark_pos[i + 1], cur_line)
					break
	
	while '@' in cur_line:
		immune_txt = ''
		imune_idx = []
		included = False
		for i in range(len(cur_line)):
			if cur_line[i] == '@':
				imune_idx.append(i)
		
		for i in raw_line:
			if i == '@':
				if included == False:
					included = True
				elif included == True:
					included = False
			elif included == True:
				immune_txt += i
		
		start_idx = imune_idx[0]
		end_idx = imune_idx[1]
		cur_str = str_in[0: start_idx] + immune_txt + str_in[end_idx + 1 : len(str_in)]