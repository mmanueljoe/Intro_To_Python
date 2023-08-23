def calculate(text,num1,num2):
	if(text.lower() == "add"):
		return num1 + num2
	elif(text.lower() == "subtract"):
		return num1 - num2
	elif(text.lower()  == "multiply"):
		return num1 * num2
	elif(text.lower() == "divide"):
		return num1 / num2
	else:
		print("Invalid Input!.Enter Operation in lower case")

add = calculate("add",2 ,3)
subtract = calculate("subtract",2 ,3)
multiply = calculate("multiply",2 ,3)
divide = calculate("divide",2 ,3)

add1 = calculate("ADD",5,5)
subtract1 = calculate("subtract",5 ,5)
multiply1 = calculate("multiply",5 ,5)
divide1 = calculate("divide",5 ,5)


print("Add: ",add)
print("Subtract: ",subtract)
print("Multiply: ",multiply)
print("Divide: ",divide)

print("\n")


print("ADD: ",add1)
print("SUBTRACT: ",subtract1)
print("MULTIPLY: ",multiply1)
print("DIVIDE: ",divide1)
