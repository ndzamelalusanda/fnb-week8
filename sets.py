...
#Sets
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Sets are unordered collections of unique elements
# They do not allow duplicate values

# Adding elements to a set
my_set.add(6)   
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Adding remove elements to a set   
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

...

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)  # or set1 | set2      
print(union_set)  # Output: {1, 2, 3, 4, 5}

#intersection of two sets
intersection_set = set1.intersection(set2)  # or set1 & set2        
print(intersection_set)  # Output: {3}  

#difference of two sets
difference_set = set1.difference(set2)  # or set1 - set2    
print(difference_set)  # Output: {1, 2}