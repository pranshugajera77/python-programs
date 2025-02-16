list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = [10, 11, 12]

set1 = set(list2)
set2 = set(list1)

set1.update(set2)
print(set1)
set1.update(list3)
print(set1)
