
# try:
#  file = open("non_exit_file.txt", 'r')

# except FileNotFoundError:
#   print("Error: The File Was Not Found")

# try:

#     number = int(input("Enter a number: "))
#     result = 10 / number

# except ValueError:
#     print("Error: Invalid input. please enter a valid number")

# except ZeroDivisionError:
#     print("Error: Division by Zero is not allowed")


# try:

#     file = open('1example.txt', 'r')

#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("Error: the file was not found!")
# finally:
#     print("Execution of the try-except block is complete.")


class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    raise CustomError("This is custom exeption")
except CustomError as e:
    print("caught custom exeption", e)


def divide(x, y):
    if y == 0:
        raise CustomError("Cannot divide by zero")
    return x / y


try:
    result = divide(10, 3)
    print("Result: ", result)

except CustomError as e:
    print("caught custom exeption:", e)
