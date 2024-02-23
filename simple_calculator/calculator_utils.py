def check_user_input(num):
    if len(num) == 1:
        print("You did not separate your numbers with a space")
        exit(-1)

    elif (num[0].isnumeric() is False) or (num[1].isnumeric() is False):
        print("Number entered is not an integer!")
        exit(-1)


def check_operation(operation):
    if not operation.isnumeric():
        print("The number you entered is not an integer")
        exit(-1)

    operation = int(operation)
    if operation not in range(1, 5):
        print("Your choice is out of range")

    return operation