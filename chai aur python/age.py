age = int(input("Enter your age: "))

if age < 13:
    print("You are child")
elif age > 13 and age < 19:
    print("You are teenagers")
elif age > 20 and age < 59:
    print("You are adult")
elif age > 60 and age < 120:
    print("You are senior")
else:
    print("You are joking right..!")
    
