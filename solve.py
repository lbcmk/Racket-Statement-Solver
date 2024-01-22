from stack import Stack

def racket_calculator(equation):
	evaluate = Stack()
	calculate = equation
	op = '+-*/'
	num = '.0123456789'
	numbers = Stack()
	ans = 0
	count = ''
	opcount = ''

	for ch in calculate:
		if(ch == '('):
			evaluate.push(ch)
		elif(ch in op):
			evaluate.push(ch)
			if (ch in '+-'):
				opcount = ch
		elif(ch in num):
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
			if (count != ''):
				evaluate.push(count)
			count = ''
			ans = 0
			while str(evaluate.top()).lstrip('+-').isdigit():
				numbers.push(int(evaluate.pop()))
			while str(evaluate.top()).lstrip('+-').replace('.', '').isdigit():
				numbers.push(float(evaluate.pop()))
			while(numbers.size() < 2):
				if(evaluate.top() in '+-'):
					numbers.push(0);
				elif(evaluate.top() in '*/'):
					numbers.push(1);
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
				raise ValueError("Incorrect Statement: Unknown symbol")
			evaluate.pop()
			evaluate.pop()
			evaluate.push(ans)
	return(ans)