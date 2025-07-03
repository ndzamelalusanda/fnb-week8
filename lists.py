# This file contains a list of fruits and apple is = 0.
#banana is = 1, cherry is = 2
fruits =["apple", "banana", "cherry"]

print(fruits[0])  # Output: apple

#list are mutable, so we can change the value of an item

fruits[1] = "blackberry"

print(fruits)  # Output: ['apple', 'blackberry', 'cherry']


#Adding appending an item to the list, meaning we can add an item to the end of the list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blackberry', 'cherry', 'orange']

#Inserting an item at a specific index
fruits.insert(1, "kiwi")   # Insert 'kiwi' at index 1 
print(fruits)  # Output: ['apple', 'kiwi', 'blackberry', 'cherry', 'orange']

#Removing an item from the list
fruits.remove("kiwi")  # Remove 'kiwi' from the list        
print(fruits)  # Output: ['apple', 'blackberry', 'cherry', 'orange']    
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blackberry', 'orange']

#Sort the list in alphabetical order
fruits.sort() #sort the list in ascending order
print(fruits)  # Output: ['apple', 'blackberry', 'orange']
#Reverse the order of the list
fruits.reverse()  # Reverse the order of the list   
print(fruits)  # Output: ['orange', 'blackberry', 'apple']