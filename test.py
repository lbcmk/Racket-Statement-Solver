from solve import *

results = []
cases = [
	'(+ 3 5)',
	'(+ (- 2 4) 5 6)',
	"(+ (- 5) 6)",
	"(+ (- 5) 6 7)",
	"(+ (- 3 5) 6)",
	"(+ 5)",
	"(- 5)",
	"(* 5)",
	"(/ 5)",
	"(- 5 3 (+ 2 6))",
	"(+)",
	"(*)",
	'(+ 3 7)',
	'(- 8 3)',
	'(* 4 6)',
	'(/ 25 5)',
	'(+ (* 7 4) (+ 3 8))',
	'(- 20.3 -5.0)',
	'(- 0 5.0)',
	'(/ 3 3 3)',
	'(/ 4000 1000)',
	'(/ 10000 10.0 10 10.0 10)',
	'(- +5 -5)',
	'(- -5 +5)',
	'(+ +5 -5)',
	'(- +5 -5)',

	'(* (+ 4 (- 3 5) 5 (/ 5 (+ 3 8))) (+ 3 5 (/ 82 (- 5 3) (* 273891275981 2371298512))))',
	'(-)',
	'(/)',
	'(-5)',
	'(5)',
	'()',
	'(.)',
	'(- - 1)',
	'(+ 1 (+ 1)',
	'(+ 1 (+ 1)))',
]

answers = [
	'8', '9', '1', '8', '4', 
	'5', '-5', '5', '0.2', '-6', 
	'0', '1', '10', '5', '24', 
	'5', '39', '25.3', '-5', '0.3333333333333333',
	'4', '1', '10', '-10', '0', 
	'10', '59.63636363636363', 'Incorrect Statement: No arguments', 'Incorrect Statement: No arguments', 'Incorrect Statement: Unknown symbol',
	'Incorrect Statement: Unknown symbol', 'Incorrect Statement: Unknown symbol', 'Incorrect Statement: Unknown symbol', 'Incorrect Statement: Contract Violation',
	'Incorrect Statement: Expected a `)` to close `(`', 'Incorrect Statement: Unexpected `)`'
]

x = True
for i in range(len(cases)):
	if(str(racket_calculator(cases[i])) != answers[i]):
		x = False;
		print(str(racket_calculator(cases[i])), answers[i])
		break;

if(x):
	print("Completed Test")
else:
	print("Failed Test")