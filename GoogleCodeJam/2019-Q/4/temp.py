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

def find_broken_machines(response, no_broken_machines):
	repeats = get_bit_repeats(no_broken_machines)
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
	print(get_bit_transition_indices("0011001010110"))
