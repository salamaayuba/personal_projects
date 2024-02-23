print("Enter two integer numbers separated by SPACE!")
n = input("Enter the two number: ")
num = n.split(" ")

if len(num) == 1:
    print("You did not separate your numbers with a space")
    exit(-1)

elif (num[0].isnumeric() == False) or (num[1].isnumeric() == False):
    print("Number entered is not an integer!")
    exit(-1)

num = [int(_) for _ in num]

print("What type of operation would you like to perform:\n"
      "Select 1 for addition\n"
      "Select 2 for subtraction\n"
      "Select 3 for multiplication\n"
      "Select 4 for division")

operation = input("Enter your choice: ")
if not operation.isnumeric():
    print("The number you entered is not an integer")
    exit(-1)

operation = int(operation)
if operation not in range(1, 5):
    print("Your choice is out of range")

if operation == 1:
    print("{} + {} = {}".format(num[0], num[1], num[0]+num[1]))

elif operation == 2:
    print("{} - {} = {}".format(num[0], num[1], num[0] - num[1]))

elif operation == 3:
    print("{} * {} = {}".format(num[0], num[1], num[0]*num[1]))

elif operation == 4:
    print("{} / {} = {}".format(num[0], num[1], num[0]/num[1]))
