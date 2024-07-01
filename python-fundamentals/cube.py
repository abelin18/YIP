# num = 10
# for n in range(1, num):
#     print(f"Current number is:{n} and the cube is {n ** 3}")

# num = 10
# for n in range(1, num):
#     print("*"*n)

# palin = input("Word: ").upper()
# for idx, p in enumerate(palin):
#     if palin[idx] == palin[-idx - 1]:
#         p = True
#     else: 
#         p = False
#         break



# print(p)


number = int(input("Number: "))
if number == 1:
    print(number, "is not prime")
elif number > 1:
    for n in range(2, number):
        if (number % n) == 0:
            print(number, "is not prime")
            break
    else: print(number, "is prime")
       
 
     
       
    
