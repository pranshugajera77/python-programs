#                find factorial number with function


def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
       fact *= i
    print(fact)

cal_fact(4)


#                convert US Dollar to IND Rupees


def con_doll(n):
    i = n*83
    print(n, "Dollar =", i, "rupees")

con_doll(5000)

#                         even or odd

n = int(input("Enter the number:"))

def eve(n):
    
    if(n % 2 == 0):
        print("even")
    else:
        print("odd")

eve(n)