# Add an element to the end of the list
my_list = [1, 2, 3]
my_list.append(4)

# Add all the elements of an iterable to the end of the list
my_list.extend([5, 6, 7])

# Insert an element at a given position in the list
my_list.insert(0, 0)

# Remove an element from the list
my_list.remove(4)

# Remove and return the last element from the list
last_element = my_list.pop()

# Remove all elements from the list
my_list.clear()

# Return the index of the first occurrence of an element in the list
index_of_2 = my_list.index(2)

# Return the number of times an element appears in the list
count_of_3 = my_list.count(3)

# Sort the elements of the list in ascending order
my_list.sort()

# Reverse the order of the elements in the list
my_list.reverse()

# Return a shallow copy of the list
my_list_copy = my_list.copy()

# Return the length of the list
length_of_list = len(my_list)

# Check if an element is in the list
is_2_in_list = 2 in my_list

# Return the largest element in the list
largest_element = max(my_list)

# Return the smallest element in the list
smallest_element = min(my_list)