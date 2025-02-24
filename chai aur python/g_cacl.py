marks = int(input("Enter your marks: "))

if marks < 100 and marks >= 90:
    print("Your grade is A")
elif marks >= 80 and marks <=89:
    print("Your grade is B")
elif marks >= 70 and marks <= 79:
    print("Your grade is C")
elif marks >= 60 and marks <= 69:
    print("Your grade is D")
elif marks >= 50 and marks <= 59:
    print("Your grade is E")
elif marks >= 0 and marks <= 49:
    print("Sorry ! You are fail..")
else:
    print("Unknown Number...! ")