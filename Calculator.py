#Ask the user to enter the first number
num1 =float(input("Enter the first number:"))

#Ask the user to enter the second 
num2 = float(input("Enter the second number:"))

#Ask the user to enter a mathematical operator of their choice
operator = input("Enter an operator (-,+,*,/):")

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":   
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
     if num2 == 0:
         print("Error!") 
     else:     
         result = num1 / num2 
         print(f"{num1} / {num2} = {result}") 
else:
    print("Invalid operator! Please use +, -, * or /")     

