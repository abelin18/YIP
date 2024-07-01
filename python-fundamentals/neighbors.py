# Given index and list of neighborhood
input("Your index: ")
index = 5
neighborhoods = [10, 7, -3, 2, 8, 9]

# Special case at end of the list
last_index = len(neighborhoods) - 1

# Get values of current position and of neighbors
current_value = neighborhoods[index]
left_value = neighborhoods[index - 1]

if index == last_index:
    right_value = neighborhoods[0]
else:
    right_value = neighborhoods[index + 1]

# If left neighbor is maximum value
if left_value >= current_value  and left_value >= right_value:
    print(f"The left neighbor has the maximum value which is {left_value}")

# If current neighbor is maximum value    
elif left_value <= current_value and current_value >= right_value:
    print(f"The current neighbor has the maximum value which is {current_value}")
# If right neighbor is maximum value
else:
    print(f"The right neighbor has the maximum value which is {right_value}")

