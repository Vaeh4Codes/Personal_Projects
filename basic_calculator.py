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

# step = digits_num / digits_num
if (digits_num == 1 ) or (digits_num % 10 == 1):
  ending = "st"
elif (digits_num == 2 ) or (digits_num % 10 == 2):
  ending = "nd"
elif (digits_num == 3 ) or (digits_num % 10 == 3):
  ending = "rd"
else:
  ending = "th"

step = 1

numbers = []
operations = []

for i in range(digits_num):
  num = int(input(f"\nWhat is the {step}{ending} number?\n"))
  numbers.append(num)
  step += 1

  operation = str(input("\nWhat's the operation?\n"))
  operations.append(operation)
  
print(f"\n {numbers}")
print(operations)

if operations[0] == "*":
  answer = numbers[0] * numbers[1]

print(answer)



