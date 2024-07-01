nums = [0, 1, 2, 3, 4, 5, 6]
evens = nums[::2]
odds = nums[1::2]
print(evens)

pets = ["Dog", "Tortoise", "Cat", "Turtle", "Hamster", "Spider", "Lizard"]
index1 = 2
index2 = 4
tails = pets[::2]
notails = pets[1:6:2]
print(tails)
Sum1 = notails[0] + notails[1] + notails[2]
Sum2 = tails[0] + tails[1] + tails[2]
print(Sum2)
txt = "I like cookies"
txt.replace