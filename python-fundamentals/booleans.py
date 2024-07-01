char = input("My index: ")
index = int(char)
bool_list = [True, True, False, False, True, False, False, False, True, True]

last_index = len(bool_list) - 1

if index == last_index:
    right_boolean = bool_list[0]
else:
    right_boolean = bool_list[index + 1]

current_boolean = bool_list[index]
left_boolean = bool_list[index - 1]
right_boolean = bool_list[index + 1] 

number_of_trues = 0
number_of_falses = 0

# equivalent for loop

idx_neighborhood = [current_boolean, left_boolean, right_boolean]

for neighbor in idx_neighborhood:
    if neighbor: 
        number_of_trues = (number_of_trues + 1)
    else: 
        number_of_falses = (number_of_falses + 1)


# if current_boolean: 
#     number_of_trues = (number_of_trues + 1)
# else: 
#     number_of_falses = (number_of_falses + 1)

# if left_boolean: 
#     number_of_trues = (number_of_trues + 1)
# else: 
#     number_of_falses = (number_of_falses + 1)

# if right_boolean: 
#     number_of_trues = (number_of_trues + 1)
# else: 
#     number_of_falses = (number_of_falses + 1)

if number_of_trues >= 2:
    print(f"The majority of the neighborhood is true: {number_of_trues}")
else:
    print(f"The majority of the neighborhood is false: {number_of_falses}")
