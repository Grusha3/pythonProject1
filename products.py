class Products:
    def __init__(self,products,bonus=0):
        self.products = products
        self.bonus = bonus
    def get_products_price(self):
        return sum(self.products.values()) - self.bonus

    def __add__(self, other):
        if isinstance(other,int):
            return Products(self.products,self.bonus + other)
        elif isinstance(other,Products):
            new_products = {}
            for product,price in self.products.items():
                if product not in new_products:
                    new_products[product] = price
            for product,price in other.products.items():
                if product not in new_products:
                    new_products[product] = price

            return Products(new_products,self.bonus + other.bonus)

    def __radd__(self, other):
        if isinstance(other,int):
            return Products(self.products,self.bonus + other)

    def __sub__(self, other):
        if isinstance(other,int):
            return Products(self.products,self.bonus-other)
        elif isinstance(other,Products):
            for product in other.products:
                if product in self.products:
                    del self.products[product]
            return Products(self.products,self.bonus - other.bonus)

    def __rsub__(self, other):
        if isinstance(other,int):
            return Products(self.products,self.bonus - other)

    def __eq__(self,other):
        return self.products == other.products

    def __str__(self):
        return f'{self.products}|{self.bonus}'

product1= Products({'кефир':2,'хлеб': 1,'кетчуп':3},6)
product2= Products({'кетчуп':3,'сосиски': 6},3)
product3 = product1 - product2
product4 = 8 - product3
print(product4)
print(product3)
print(product1.get_products_price())
#полиморфизм
