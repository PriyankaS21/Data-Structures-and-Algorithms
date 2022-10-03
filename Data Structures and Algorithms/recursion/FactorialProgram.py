# Fibonacci Series
'''
def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

count = 6

if count <= 0:
    print("Please enter the value mor ethan 2")
else:
    for i in range(count):
        print(fib(i), end=" ")
'''

# if want to print the no
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return (fib(n-1) + fib(n-2))

# count = 6

# if count <= 0:
#     print("Please enter the value mor ethan 2")
# else:
#     for i in range(count):
#         last_value = fib(i)
#     print(last_value)

# if want sum of fibo series
def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

count = 6

if count <= 0:
    print("Please enter the value more than 2")
else:
    sum = 0
    for i in range(count):
        sum = sum + fib(i)
    print(sum)