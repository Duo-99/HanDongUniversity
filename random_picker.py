import random as rn

def getting_name(num_1):
    names = []
    for i in range(num_1):
        get_name = input("Enter a name: ")
        names.append(get_name)
    return names

num_1 = int(input("Enter the number of people: "))
names = getting_name(num_1)
result = rn.randint(0, num_1 - 1)


choosing_name = names[result]
print(f"{choosing_name} is going to buy the meal.")

