import sys

def get_alternate_route(route):
	new_route = ""
	for step in route:
		if step == 'E':
			new_route = new_route + 'S'
		else:
			new_route = new_route + 'E'
	return new_route

def main():
	cases = int(sys.stdin.readline().rstrip())
	iteration = 1
	while iteration <= cases:
		grid_size = sys.stdin.readline()
		moves = sys.stdin.readline().rstrip()
		print("Case #%d:" % iteration, get_alternate_route(moves))
		iteration += 1

if __name__ == "__main__":
	main()