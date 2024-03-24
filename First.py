# string_1 = [1,2,3,4,5,6,'M']
# string_2 = [7,8,8,9,10,'W']

# print("Here is Two string.")

# str_3 = string_1 +string_2

# if 'W' in str_3:
#     print("W is here.")
#     num = str_3.index('W')
#     print(str_3[:num+1])
# elif 'H' in str_3:
#     print("H is here.")
    
# if 'M' in str_3:
#     print("M is here.")
#     num = str_3.index('M')
#     print(str_3)
# else:
#     print("Nothing is here.")

# import sys

# x = 10
# print("Get size of number : {} bytes.".format(sys.getsizeof(x)))
    
    
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # Your code below
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"

# print(f"{line1}\n{line2}\n{line3}")
my_list = [10,20,30,40]
for i in my_list:
    print(i)
    
for x,y in enumerate(my_list):
    print(x,y)