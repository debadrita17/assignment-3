#assignment3
#task1
#WAP to calculate factorial using a function(loop or recursion) & take a number as an argument.
#returns the calculated factorial & calls the function with a sample number & prints the output.
#using recursion

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
result = fact(int(input("enter a number: ")))
print("factorial of 7 is:" , result)


#using loop
def fact(n):
    v = 1
    for i in range(1 , n + 1):
        v *= i
    return v
result = fact(int(input("enter a number: ")))
print("factorial of 7 is:" , result)























