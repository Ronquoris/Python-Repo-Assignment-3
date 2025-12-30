
def factorial(num):
    if num == 0 or num == 1:
        #print ("u tesing me or wat?")
        return 1
    else:
        return num*factorial(num-1)
    

n=int(input("Enter a number to find factorial: "))
fact=factorial(n)
print(f"The factorial of {n} is {fact}")
