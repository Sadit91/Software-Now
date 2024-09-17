global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

# Set (fixed: duplicate values removed)
my_set = {1, 2, 3, 4, 5}  # Sets automatically ignore duplicates
result = process_numbers()  # Removed argument that was incorrectly passed

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

modify_dict()  # Fixed: removed incorrect argument being passed

# Function to update the global variable
def update_global():  # Fixed typo in function name from 'upcate_global' to 'update_global'
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)  # Fixed: removed unnecessary 'i += 1', as 'for' loop controls iteration automatically

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")  # Fixed typo: 'Conditon' corrected to 'Condition'

if 5 not in my_dict:
    print("5 not found in the dictionary!")  # Fixed typo: 'dictionaryy' corrected to 'dictionary'

print(global_variable)
print(my_dict)
print(my_set)