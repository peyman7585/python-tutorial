
def greet(name):
    print(f"Hello {name}")


greet("Alice")


def add(a, b):
    return a + b


result = add(45, 56)
print(f"The sum is {result}")


def greeting(name, greeting="Hello"):

    return f"{greeting} {name}"


print(greeting("sarah"))
print(greeting("jenny", "hey"))


def get_min_max(number):

    return min(number), max(number)


nums = [9, 1, 2, 4, 6, 7]

minimum, maximum = get_min_max(nums)
print("Minimum:", minimum)
print("Maximum", maximum)

z = 30


def my_function():
    global z
    z = 45
    print("Inside the function z:", z)


print("Before calling the function z:", z)
my_function()
print("After calling the function z:", z)
