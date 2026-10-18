from inventory import inventory
from product import Electronics, Clothes, Food
obj1 = inventory()
def show_menu():
    print("===== Inventory Management System =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Get Total Value")
    print("6. Get Low Stock")
    print("7. Exit")
    print("========================================")
def products_menu():
    print("========================================")
    print("A. Electronics")
    print("B. Clothes")
    print("C. Food")
    print("========================================")
while True:
    show_menu()
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        products_menu()
        choice1 = input("Enter Your Choice: ")
        if choice1 == "A":
         name = input("Enter Product name: ")
         quantity = int(input("Enter Quantity of Products: "))
         price = int(input("Enter Price of Product: "))
         warranty = input("Enter Product Warranty: ")
         p4 = Electronics(name,price,quantity,"Electronics",warranty)
         obj1.add_product(p4)
         print(p4.product_info())
         print("Product is added successfuly.")
        elif choice1 == "B":
         name = input("Enter Product name: ")
         quantity = int(input("Enter Quantity of Products: "))
         price = int(input("Enter Price of Product: "))
         size = input("Enter the Size: ")
         p5 = Clothes(name,price,quantity,"Cloths",size)
         obj1.add_product(p5)
         print(p5.product_info())
         print("Product is added successfuly.")
        elif choice1 == "C":
         name = input("Enter Product name: ")
         quantity = int(input("Enter Quantity of Products: "))
         price = int(input("Enter Price of Product: "))
         category = input("Enter Category: ")
         manufacture = input("Enter Manufacture Date: ")
         expiry = input("Enter the Expiry Date: ")
         p6 = Food(name,price,quantity,category,manufacture,expiry) 
         obj1.add_product(p6)
         print(p6.product_info())
         print("Product is added successfuly.")
        else:
           print("Please Chose between A to C.")
           continue
    elif choice == 2:
        name = input("Enter Product name: ")
        obj1.remove_product(name)
        print("Product is Removed successfuly.")
    elif choice == 3:
        category = input("Enter Category: ")
        name = input("Enter Product name: ")
        obj1.search_product(name)
        if category == "Electronics":
         print(p4.product_info())
         print("Product is Searched successfuly.")
        elif category == "Cloths":
         print(p5.product_info())
         print("Product is Searched successfuly.")
        else:
         print(p6.product_info())
         print("Product is Searched successfuly.")
    elif choice == 4:
        name = input("Enter Product name: ")
        quantity = int(input("Enter Quantity of Products: "))
        price = int(input("Enter Price of Product: "))
        obj1.update_product(name,quantity,price)
        print("Product is Updated successfuly.")
    elif choice == 5:
        Total = obj1.get_totalvalue()
        print(Total)
    elif choice == 6:
        Low = obj1.get_lowstock()
        print(Low)
    elif choice == 7:
        print("Exit Successfuly")
        break
    else:
        print("Enter Choice Between 1 to 7.")
        