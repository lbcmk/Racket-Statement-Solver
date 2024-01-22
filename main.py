from solve import *

if(__name__ == "__main__"):
	x = 0;
	while(x != ValueError):
		case = input("Type the racket you want calculated, or type 'end' to exit: ")
		if(case == 'end'):
			break;
		elif('end' in case):
			case = input("Do you want to exit? (y/N): ")
			if(case == 'Y' or case == 'y'):
				break;
		else:
			try:
				x = racket_calculator(case)
				print("Result:", x);
			except ValueError:
				print("Incorrect Statement: Unknown symbol")