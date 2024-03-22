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

item1 = item('Laptop', 'Lenovo',  500, 2)
item2 = item('Phone', 'Samsung', 250, 4)
item2.pay_rate = 0.7
print(item1.calculate())
print(item2.calculate())

print(item1.__dict__)