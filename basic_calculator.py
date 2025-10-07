#This is a basic 4 function calculator that presents an ascii art immage of the operaions abaialbe. Then, the user is asked to input their operations. The computer will then ouptu the answer. 

print("\nWelcome to Nevaeh's 4-function calculator!")
print("""
 ________________________________
|   __________________________   |
|  |         Caclulator       |  |
|  |__________________________|  |
|   _____ _____ _____    _____   |
|  |  7  |  8  |  9  |  |  +  |  |
|  |_____|_____|_____|  |_____|  |
|  |  4  |  5  |  6  |  |  -  |  |
|  |_____|_____|_____|  |_____|  |
|  |  1  |  2  |  3  |  |  x  |  |
|  |_____|_____|_____|  |_____|  |
|  |  .  |  0  |  =  |  |  /  |  |
|  |_____|_____|_____|  |_____|  |
|                                |
|________________________________|

""")

digits_num = int(input("How many numbers are in your expression?\n"))

expression = []

for i in range(1, digits_num + 1, 1):
  num = str(input(f"\nWhat is the {i} number?: "))
  expression.append(num)

  operation = str(input("\nWhat's the operation? If you are finished type ""done"": "))
  if operation == "done":
    break
  else:
    expression.append(operation)


equation = "".join(expression)
answer = eval(equation)

print(f"\n{equation} = \n {answer}")






