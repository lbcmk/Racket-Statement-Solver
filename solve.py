from stack import Stack

def racket_calculator(equation):
	evaluate = Stack()
	op = '+-*/'
	num = '.0123456789'
	numbers = Stack()
	ans = 0
	count = ''
	opcount = ''
	brackets = 0

	for ch in equation:
		if(ch == '('):
			evaluate.push(ch)
			brackets += 1
		elif(ch in op):
			evaluate.push(ch)
			if (ch in '+-*/'):
				opcount = ch
		elif(ch in num):
			if(opcount == '/' or opcount == '*'):
				return ValueError("Incorrect Statement: Unknown symbol")
			if (opcount == '-' or opcount == '+'):
				count += opcount
				evaluate.pop()
				opcount = ''
			count += ch
		elif(ch == ' '):
			opcount = ''
			if (count != ''):
				evaluate.push(count)
				count = ''
		elif(ch == ')'):
			brackets -= 1;
			if(brackets < 0):
				return ValueError("Incorrect Statement: Unexpected `)`")
				
			if (count != ''):
				evaluate.push(count)
			count = ''
			ans = 0
			while(check_digit(evaluate.top())):
				numbers.push(float(evaluate.pop()))
					
			if(numbers.size() == 0 and str(evaluate.top()) in '-/'):
				return ValueError("Incorrect Statement: No arguments")
				
			while(numbers.size() < 2):
				if(str(evaluate.top()) in '*/'):
					numbers.push(1);
				else:
					numbers.push(0);

			if(evaluate.top() == '+'):
				ans += numbers.pop()
				while(numbers.size() > 0):
					ans += numbers.pop()
			elif(evaluate.top() == '-'):
				ans = numbers.pop()
				while(numbers.size() > 0):
					ans -= numbers.pop()
			elif(evaluate.top() == '*'):
				ans = numbers.pop()
				while(numbers.size() > 0):
					ans *= numbers.pop()
			elif(evaluate.top() == '/'):
				ans = numbers.pop()
				while(numbers.size() > 0):
					ans /= numbers.pop()
			else:
				return ValueError("Incorrect Statement: Unknown symbol")
			evaluate.pop()
			if(evaluate.pop() != '('):
				return ValueError("Incorrect Statement: Contract Violation")
			evaluate.push(ans)
		else:
			return ValueError("Incorrect Statement: Unknown symbol")
	if(brackets != 0):
		return ValueError("Incorrect Statement: Expected a `)` to close `(`")

	if(int(ans) == ans):
		return(int(ans))
	else:
		return(ans)


def check_digit(number):
	try:
		float(number)
		return True
	except ValueError:
		return False