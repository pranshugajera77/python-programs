#                          update Method

print("Update Method :-")
set1 = {"c", "d", "a", "a", "b", "b", "a"}  # this is a set
tup1 = ("c", "d", "a", "a", "b", "b", "a")  # this is a tuple
list1 = ["c", "d", "a", "a", "b", "b", "a"]  # this is a list

set1.update("f")
print(set1)

tup2 = list(tup1)
tup2[1] = "g"
tup1 = tuple(tup2)
print(tup1)

list1[1] = "p"
print(list1)


#                       access method
print("Access Method :-")

set1 = {"Apple", "Banana", "Cherry", "Mango"}  # this is a set
tup1 = ("Apple", "Banana", "Cherry", "Mango")  # this is a tuple
list1 = ["Apple", "Banana", "Cherry", "Mango"]  # this is a list

set1 = tuple(set1)
print(set1[0:2])

print(tup1[0:3])

list1 = tuple(list1)
print(list1[0:1])

#                        delete method

print("Delete Method :-")
set1 = {"Apple", "Banana", "Cherry", "Mango"}  # this is a set
tup1 = ("Apple", "Banana", "Cherry", "Mango")  # this is a tuple
list1 = ["Apple", "Banana", "Cherry", "Mango"]  # this is a list

set1.remove("Banana")
print(set1)

tup1 = set(tup1)
tup1.remove("Apple")
print(tup1)

list1 = set(tup1)
list1.remove("Banana")
print(list1)