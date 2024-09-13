'''
STRINGS
'''

#Initialize
str1 = "Hello"
str2 = "World"
str3 = "apple,orange,banana"
str4 = "a"
str5 = "0"
string_builder = [str1]

string_builder.append(str2) # Concatenate: -- [Hello, World] -- faster than str += str

REPITITION = str1* 3 # Repitition: HelloHelloHello
LENGTH = len(str1) # Length: 5
CHAR = str1[0] # char: H
SUBSTRING = str1[1:4] # substring: ell
UPPERCASE = str1.upper() # uppercase: HELLO
LOWERCASE = str2.lower() # lowercase: world
STRIP = s.strip() # REMOVES WHITE SPACE
str4_bool = str4.isalpha() # check is alphabet: returns True
str5_bool = str5.isdigit() # check is digit: returns True
str1 = sorted(str1) # sorts string: ['H', 'e', 'l', 'l', 'o']

# ------------------------------------------------------------------
#ASCII VALUES
# Find ASCII with ord() method
# Print char with ASCII with chr method: chr(65) --> "A"

# 32: " "     33: !     34: "     35: #     36: $     37: % 

# 38: &     39: '     40: (     41: )     42: *     43: + 

# 44: ,     45: -     46: .     47: /

print(ord("0")) # outputs: 48
print(ord("9")) # outputs: 57

# 58: :     59: ;     60: <     61: =     62: >     63: ?     64: @

print(ord("A")) # outputs: 65
print(ord("Z")) # outputs: 90

# 91: [     92: \     93: ]     94: ^     95: _     96: `

print(ord("a")) # outputs: 97
print(ord("z")) # outputs: 122

# 123: {     124: |     125: }     126: ~

#Main Idea:
#0-31      Control characters (e.g., newline, tab)
#32-126    Printable characters (e.g., letters, digits, punctuation)
#127       (Delete)    May vary in extended ASCII sets
# ------------------------------------------------------------------

'''
LISTS
'''
#  Initialize
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] # initialize array with content
my_list = [0] * SIZE # initialize array of some size


# Modifying Content
my_list.append(8) # adds to end of the list
my_list.insert(2, 7) # inserts at specific index
my_list.remove(5) # deletes at specific index
my_list.clear() # removes all elements from the list
popped_value = my_list.pop(4) # deletes and retuns element at specific index
my_list.sort() # sorts the elements of the list in ascending order
my_list.sort(reverse=True) # sorts the elmeents of the list in descending order
my_list.reverse() # reverses the order of elements in the list

#Evaluating Content
index_of_6 = my_list.index(6) # find method (returns first occurence of specific element)
count_of_3 = my_list.count(3) # returns the number of occurrences of a specific element
length_of_list = len(my_list) # returns the number of elements in the list

'''
HASHING
'''
# Initialize*
my_dict = {'key1': 'value1'}
my_dict = {}

# Accessing Values
value = my_dict['key1']

# Adding or Updating Key-Value Pairs
my_dict['new_key'] = 'new_value'
my_dict.update({'key1': 'updated_value'})

# Removing Key-Value Pairs
removed_value = my_dict.pop('key2', None)  # Returns and removes key-value pair, None if key not found
del my_dict['key3']  # Removes key-value pair

# Getting Keys, Values, and Items
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

# Check if Key Exists
key_exists = 'key1' in my_dict

# Get Value with Default
default_value = my_dict.get('nonexistent_key', 'default_value')

# Clearing the Dictionary
my_dict.clear()

# Copying a Dictionary
copied_dict = my_dict.copy()