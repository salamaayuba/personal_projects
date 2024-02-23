import calculator_utils, calculator_functions


def main():
      print("Enter two integer numbers separated by SPACE!")
      num = input("Enter the two number: ").split(" ")

      calculator_utils.check_user_input(num)

      num = [int(_) for _ in num]

      print("What type of operation would you like to perform:\n"
            "Select 1 for addition\n"
            "Select 2 for subtraction\n"
            "Select 3 for multiplication\n"
            "Select 4 for division")

      operation = input("Enter your choice: ")
      operation = calculator_utils.check_operation(operation)
      calculator_functions.calculate(operation, num[0], num[1])


if __name__ == "__main__":
      main()
