#tuples are immutable sequences of objects
#they are defined by enclosing the elements in parentheses 
#tuples can be used to store multiple items in a single variable

#creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3
print(my_tuple[-1])  # Output: 5

tuple1 =(1, 2, 3) # Creating a tuple with different data types
tuple2 = (4, 5, 6) # Concatenating tuples

conc_tuple = tuple1 + tuple2  # Concatenating tuples
print(conc_tuple)  # Output: (1, 2, 3, 4, 5, 6)

#repeating tuples
repeated_tuple = tuple1 * 3  # Repeating the tuple
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)