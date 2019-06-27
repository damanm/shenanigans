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

def find_no_broken_machines(response, start_index, end_index, char):
	no_broken_machines = 0
	for index in range(start_index, end_index+1):
		if char != response[index]:
			no_broken_machines = end_index-index+1
			break
	return no_broken_machines

def get_broken_machine_map(response, repeats):
	chars = ['0', '1']
	to_find = 0
	count = 0
	map = []
	index = 0
	while(index<len(response)):
		end_index = repeats+index-1 if (repeats+index-1) < len(response) else len(response) - 1
		no_broken = find_no_broken_machines(response, index, end_index, chars[to_find])
		map.append([end_index, no_broken])
		to_find=to_find^1
		index = end_index+1-no_broken
	return map

def find_broken_machines(no_bits, no_broken_machines):
	# get repeats for number of broken machines
	repeats = get_bit_repeats(no_broken_machines)
	
	# generate test string to query the system
	test_string = generate_bit_string(no_bits, repeats)
	
	# query the system
	response = query_system(test_string)
	
	# identify number of broken machines in each section of test_string
	bit_trans = get_bit_transition_indices(response)

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
	output = get_broken_machine_map("001101", 2)
	print(output)
