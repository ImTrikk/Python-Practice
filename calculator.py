num1 = int(input("Enter value for num1: "))
num2 = int(input("Enter value for num2: "))

opr = str(input("Enter operator [+, -, /, *]: "))

match opr:
	case "+":
				print(num1 + num2)
	case "-":
			print(num1 - num2)
	case "/":
			if num2 == 0: 
					print("Cannot divide by 0")
			else: 
					print(num1 / num2)
	case "*":
			print(num1 * num2)