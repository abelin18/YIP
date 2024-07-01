
# if "red" in aidan_fav_colors:
#     colors_in_common.append("red")
# if "green" in aidan_fav_colors:
#      colors_in_common.append("green")
# if "blue" in aidan_fav_colors:
#     colors_in_common.append("blue")
# print(colors_in_common)

sam_fav_colors = ["orange", "black", "blue"]
red_fav_colors = ["red", "black", "yellow"]
oumy_fav_colors = ["purple", "green", "pink"]
ethan_fav_colors = ["blue", "red", "green"]
aidan_fav_colors = ["blue", "red", "green"]  
colors_in_common = []

# using for loops
for color in aidan_fav_colors:
    if color in red_fav_colors:
        print(f"These two have favorite colors in common")

# using while loops
e_count = 0
idx = 0
names = ["Fred", "Jazz", "Blake", "Ethan", "Red", "Olivia", "Benji", "Neel", "Oumy", "George"]
# while(e_count < 3):
#     name = names[idx]
#     if ("e" in name):
#         print(name)
#         e_count += 1
#     idx += 1



color_count = 0
idx = 0
while(color_count < 3):
    aidan_color = aidan_fav_colors[idx]
    if aidan_color in ethan_fav_colors:
        print(f"{aidan_color}")
    color_count += 1
    idx += 1
    