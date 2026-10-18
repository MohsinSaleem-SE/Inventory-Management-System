from product import Clothes, Electronics, Food
class inventory:
    def __init__(self):
        self.products = [ ]
    def add_product(self,product):
        self.products.append(product)
    def remove_product(self, name):
        for p in self.products:
          if p.name == name:
            self.products.remove(p)
            return p.product_info()
    def search_product(self,name):
        for p in self.products:
          if p.name == name:
           return p.product_info()
    def update_product(self,name,new_quantity,new_price):
        for p in self.products:
          if p.name == name:
             p.quantity = new_quantity
             p.price = new_price
             return p.product_info()
    def get_totalvalue(self):
        total = 0
        for p in self.products:
          total = total + (p.price * p.quantity)
        return f"Total Amount is: {total}"
    def get_lowstock(self):
        for p in self.products:
         if p.quantity<5:
          return f"{p.category} has Low Stock."

# obj1 = inventory()
# p1 = Electronics("Laptop",180000,2,"Electronics","3 Years")
# p2 = Clothes("Tshirt",800,2,"Cloths","Medium")
# p3 = Food("Apple",3000,12,"Fruits","03/04/2026","05/04/2026")

# obj1.add_product(p1)
# obj1.add_product(p2)
# obj1.add_product(p3)
# print(obj1.products[0].product_info())
# print(obj1.remove_product("Laptop"))
# print(obj1.search_product("Tshirt"))
# print(obj1.update_product("Apple",5,250))
# for p in obj1.products:
#     print(p.product_info())
# print(obj1.get_totalvalue())
# print(obj1.get_lowstock())
