from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    @abstractmethod
    def product_info(self):
        pass
class Electronics(Product):
    def __init__(self, name, price, quantity, category,waranty):
        super().__init__(name, price, quantity, category)
        self.waranty = waranty
    def product_info(self):
        return f"|| Electronics Products || \nName: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nCategory: {self.category}\nWarranty: {self.waranty}\n"
class Clothes(Product):
    def __init__(self, name, price, quantity, category, size):
        super().__init__(name, price, quantity, category)
        self.size = size
    def product_info(self):
        return f"|| Clothing Products || \nName: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nCategory: {self.category}\nSize: {self.size}\n"    
class Food(Product):
    def __init__(self, name, price, quantity, category, mDate, exDate):
        super().__init__(name, price, quantity, category)
        self.mDate = mDate
        self.exDate = exDate
    def product_info(self):
        return f"|| Food Products || \nName: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nCategory: {self.category}\nManufacturing Date: {self.mDate}\nExpiry Date: {self.exDate}"

# obj1 = Electronics("Laptop",180000,2,"Electronics","3 Years")
# obj2 = Clothes("Tshirt",800,2,"Cloths","Medium")
# obj3 = Food("Apple",3000,"2kg","Fruits","03/04/2026","05/04/2026")
# print(obj1.product_info())
# print(obj2.product_info())
# print(obj3.product_info())






    