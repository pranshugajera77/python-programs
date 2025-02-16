#                            Recursive function

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END")
    
show(1)

#                       Find Factorial with recursive function

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return fact(n - 1) * n
print(fact(4))
    
