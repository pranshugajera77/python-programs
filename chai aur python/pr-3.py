# List Operations
my_list = [1, 2, 3]
# Create
my_list.append(4)
print("List after Create:", my_list)
# Read
print("Read element at index 1:", my_list[1])
# Update
my_list[1] = 10
print("List after Update:", my_list)
# Delete
my_list.remove(10)
print("List after Delete:", my_list)

# Tuple Operations (Tuples are immutable, so we recreate the tuple)
my_tuple = (1, 2, 3)
# Create (Recreate tuple)
my_tuple = my_tuple + (4,)
print("Tuple after Create:", my_tuple)
# Read
print("Read element at index 1:", my_tuple[1])

# Set Operations
my_set = {1, 2, 3}
# Create
my_set.add(4)
print("Set after Create:", my_set)
# Read
print("Check if 3 exists in set:", 3 in my_set)
# Update (remove and add)
my_set.remove(2)
my_set.add(10)
print("Set after Update:", my_set)
# Delete
my_set.remove(10)
print("Set after Delete:", my_set)

# Dictionary Operations
my_dict = {'a': 1, 'b': 2}
# Create
my_dict['c'] = 3
print("Dictionary after Create:", my_dict)
# Read
print("Read value of key 'a':", my_dict['a'])
# Update
my_dict['a'] = 10
print("Dictionary after Update:", my_dict)
# Delete
del my_dict['b']
print("Dictionary after Delete:", my_dict)