class item:
    pay_rate =  0.8 #20%discount
    def __init__(self, name : str, model, price : float, quantity =0):
        assert price >= 0, f'price must be greater than zero.'
        assert quantity >= 0, f'quantity must be at least one'
        
        self.name = name
        self.model= model
        self.price = price
        self.quantity = quantity
    def calculate(self):
        return self.price * self.quantity * self.pay_rate

item1 = item(2303, 'Lenovo',  500, 2)
item2 = item('Phone', 'Samsung', 250, 4)
item2.pay_rate = 0.7
print(item1.calculate())
print(item2.calculate())

print(item1.__dict__)

# use to accept only numbers

# def get_integer_input(prompt):
#     while True:
#         user_input = input(prompt)
#         try:
#             integer_value = int(user_input)
#             return integer_value
#         except ValueError:
#             print("Please enter a valid integer.")

# number = get_integer_input("Please enter an integer: ")
# print("You entered:", number)

# use to accept only letter

# def get_letter_input(prompt):
#     while True:
#         user_input = input(prompt)
#         if user_input.isalpha():
#             return user_input
#         else:
#             print("Please enter letters only.")

# letters = get_letter_input("Please enter letters only: ")
# print("You entered:", letters)

# import random as rn

# random = rn.random()
# print(random)


