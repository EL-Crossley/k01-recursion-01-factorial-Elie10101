3# Put your function here
def factorial(x):
    if x == 1:
        return 1
    # base case
    else:
        return x * (factorial(x-1))
    # general case

# testing
num = int(input())
print(factorial(num))