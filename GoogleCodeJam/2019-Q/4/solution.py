import sys

def get_bit_repeats(broken_workers):
	for i in range(4):
		if broken_workers // 2**i == 1:
			return 2**i
	exit()

def generate_bit_string(length, repeat):
	string = ""
	strings = ['0'*repeat, '1'*repeat]
	char = 0
	full_repeats = length // repeat
	for full_repeat in range(full_repeats):
		string += strings[char]
		char = char^1
	string += (str(char)*(length%repeat))
	return string

def get_bit_transition_indices(response):
	indices = []
	chars = ['0', '1']
	to_find = 1
	for i in range(len(response)):
		if(response[i] == chars[to_find]):
			indices.append(i)
			to_find = to_find^1
	return indices

def query_system(test_string):
	print(test_string, flush=True)
	return sys.stdin.readline().rstrip()

def find_no_broken_machines(response, start_index, repeats, char):
	print("start: %d | repeats: %d" % (start_index, repeats))
	no_broken_machines = 0
	count = 0
	index = start_index
	while(index<len(response) and count < repeats):
		if char == response[index]:
			count+=1
		else:
			break
		index+=1
	no_broken_machines = repeats-count
#	for index in range(start_index, end_index+1):
#		if char != response[index]:
#			no_broken_machines = end_index-index+1
#			break
	return no_broken_machines

def get_broken_machine_map(response, no_broken_machines):
	chars = ['0', '1']
	to_find = 0
	found_broken_machines = 0
	map = []
	index = 0
	repeats = get_bit_repeats(no_broken_machines)
	while(found_broken_machines < no_broken_machines):
#		end_index = repeats+index-1 if (repeats+index-1) < len(response) else len(response) - 1
		# calculate indices of sector of bits in original test_string from where bits are missing
		sector_start = index + found_broken_machines # accounting for the missing bits by adding already identified broken machines
		sector_end = sector_start+repeats-1
		
		# find number of broken bits in sector
		no_broken = find_no_broken_machines(response, index, repeats, chars[to_find])
		
		# add info to map
		map.append([sector_start, sector_end, no_broken])
		
		# update count of found broken machines
		found_broken_machines += no_broken
		
		# update character to look for
		to_find=to_find^1
		
		# update index to start of next sector in response string
		index = index+repeats-no_broken
	return map

def find_broken_machines(total_no_bits, no_broken_machines):
	# get repeats for number of broken machines
	repeats = get_bit_repeats(no_broken_machines)
	
	# generate test string to query the system
	test_string = generate_bit_string(total_no_bits, repeats)
	
	# query the system
	response = query_system(test_string)
	
	# identify number of broken machines in each section of test_string
	broken_machine_map = get_broken_machine_map(response, no_broken_machines)
	
	broken_machines = []
	
	while(True):
		for entry in map:
			# bit has been tracked down
			if entry[0] == entry[1]:
				broken_machines.append(entry[0])
			# entire bit sequence missing in response -> multiple bits tracked!
			elsif: entry[1]-entry[0] == entry[2]
				for i in range(entry[0],entry[1]+1):
					broken_machines.append(i)
		if len(broken_machines) == no_broken_machines;
			break
		# there are broken machines to be found

def main():
	cases = int(sys.stdin.readline().rstrip())
#	print("Cases: ", cases)
	for iteration in range(1,cases+1):
		input_data = sys.stdin.readline().rstrip().split()
		for i in range(3):
			input_data[i] = int(input_data[i])
		test_string = generate_bit_string(input_data[0], get_bit_repeats(input_data[1]))
		print(test_string, flush=True)
		response_string = sys.stdin.readline().rstrip()
		
		

if __name__ == "__main__":
#	main()
#	for i in range(1,16):
#		print("%d %d" % (i, get_bit_repeats(i))
	output = find_broken_machines(8, 2)
#	output = find_no_broken_machines("001100", 0, 2, '0')
#	print(output)
#	output = find_no_broken_machines("001100", 2, 2, '1')
#	print(output)
#	output = find_no_broken_machines("001100", 4, 2, '0')
#	print(output)
#	output = find_no_broken_machines("001100", 6, 2, '1')
	print(output)
