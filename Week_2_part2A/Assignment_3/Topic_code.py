#List:

# Example of list operations
my_list = [1, 2, 3, 4, 5]

# Append and extend operations
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

my_list.extend([7, 8, 9])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehensions
squared = [x ** 2 for x in my_list]
print(squared)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]



#String:

# Example of string methods
my_string = "Hello, World!"

# Split and join operations
split_string = my_string.split(", ")
print(split_string)  # Output: ['Hello', 'World!']

joined_string = "-".join(split_string)
print(joined_string)  # Output: Hello-World!

# String formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Alice and I am 30 years old.


#Fuctions:

# Example of defining functions
def greet(name):
    return f"Hello, {name}!"

def add_numbers(x, y):
    return x + y

print(greet("Alice"))  # Output: Hello, Alice!
print(add_numbers(3, 5))  # Output: 8

# Lambda function
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6
