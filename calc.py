def f(x):
		return {
			'+': int(num1) + int(num2),
			'-': int(num1) - int(num2),
			'*': int(num1) * int(num2),
			'/': int(num1) / int(num2)
		}.get(x, "Enter a valid operator (+,-,*,/)")

while True:
	num1 = input("\nEnter a number,or press a letter to exit\n")
	if num1.isdigit() != True:
		break
	y = input("Enter the operator\n")
	num2 = input("Enter the 2nd number\n")
	if num2.isdigit() != True:
		print("The 2nd NUMBER has to be a NUMBER as well")
		continue
	print("Result:", f(y))

