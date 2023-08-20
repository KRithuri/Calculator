# define functions needed
def add(x, y):
    answer = x + y
    return answer

def subtraction(x, y):
    answer = x - y
    return answer

def multiplication(x, y):
    answer = x * y
    return answer

def division(x, y):
    answer = x / y
    return answer

# print options to the user
print("Select operation: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide")

# while loop to continue or exit the program
while True:
    # take input from the user
    choice = input("Enter choice (1/2/3/4): ")
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid! Enter a number.")
            continue

        if choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))
        elif choice == '2':
            print(num1, '-', num2, '=', subtraction(num1, num2))