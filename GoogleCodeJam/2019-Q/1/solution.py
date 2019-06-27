import sys

def split_number(number):
	first, second = [], []
	for value in number:
		if (4 == value):
			first.append(1)
			second.append(3)
		else:
			first.append(value)
			second.append(0)
	return [first, second]

def get_first_number(source):
#	print("Source string = ", source),
	number = ""
	for char in source:
#		print(char)
		if ('4' == char):
			number = number + ('3')
		else:
			number = number + (char)
	return number

def main():
	iteration = 1
	cases = int(sys.stdin.readline().rstrip())
	while iteration <= cases:
		input = sys.stdin.readline().rstrip()
		first = get_first_number(input)
		second = int(input) - int(first)
		print("Case #%d:" % iteration , first, second, sep=' ')
		iteration += 1


if __name__ == "__main__":
	main()