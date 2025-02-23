day = int(input("Enter the day: "))
age = int (input("Enter your age: "))

if age == 18 and age > 18:
    price = 200
    print("Your ticket is: ", price)
elif age < 17 and age > 1:
    price = 100
    print("Your ticket is: ",price)
elif age <= 100:
    price = 200
    print("Your ticket is: ", price)
else:
    print("You are joking right...!")
    
if day == 5:
    disc = int(price / 2)
    print("with discount your ticket is:", disc)
elif day >= 8:
    print("You are joking right now")
else:
    print("no any discount")
    print("Your price is regular")