# Case one
colors = ["Blue", "Green", "Purple", "Red"]
index1 = 0
index2 = 3

oldcolor = colors[index2]
print(colors)
colors[0] = colors[index1]
colors[3] = oldcolor
# Case two
colors = ["Blue", "Purple", "Green", "Red"]
index1 = 1
index2 = 2

oldcolor = colors[index2]
print(colors)
colors[1] = colors[index1]
colors[2] = oldcolor 
#Case three 
nums = [1, 5, 7, 6, 8, 11, 12]

index1 = 2
index2 = 4

oldnums = nums[index1]
nums[2] = nums[index2]
nums[4] = oldnums
print(nums)
