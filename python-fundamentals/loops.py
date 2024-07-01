# nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  
# randomnums = []
# for n in randomnums:
#     if n % 2 == 0: 
#        nums.append(n)
# print(nums)

# lst = ["apple", "banana", "pear"]
# lst2 = []
# var = "cat"
# for word in lst:
#     lst2.append(word)
#     lst2.append(var)
# print(lst2)

# lst = [5, 6, 8, 2, -5]
# lst2 = []
# boolean = "True"
# for word in lst: 
#     lst2.append(word)
#     lst2.append(boolean)
# print(lst2)

# lst1 = ["apple", "banana", "orange"]
# # lst2 = ["cat", "dog"]
# # lst3 = []
# # for word in lst1:
# #         lst3.append(word)
# #         lst3.extend(lst2)
# # print(lst3)

# lst1 = ["cake", "cookies", "cupcake"]
# lst2 = ["eggs", "flour", "sugar"]
# lst3 = []
# for word in lst1:
#     lst3.append(word)
#     lst3.extend(lst2)
# print(lst3)
lst1 = ["apple", "banana", "pear"]
lst2 = ["cat", "dog"]

final_lst = []
for fruit in lst1:
    final_lst.append(fruit)

    for pet in lst2:
        final_lst.append(pet)
    print(final_lst)
