super_heroes = "spider man"

for el in super_heroes:
    if(el == 'r'):
       print("r Found")
       break
    print(el)
else:
    print("the loop is end")
    
print(type(super_heroes))


nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 64)
x = 49

idx = 0
for el in nums:
    if(el == x):
        print("the number is found", idx)
        idx += 1    