products = []

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity sold: "))
    price = float(input("Enter price per item: "))
    products.append({"name": name, "quantity": quantity, "price": price})
    print("Product record added!")

def update_product():
    name = input("Enter product name to update: ")
    for product in products:
        if product["name"].lower() == name.lower():
            product["quantity"] = int(input("Enter new quantity sold: "))
            product["price"] = float(input("Enter new price: "))
            print("Product record updated!")
            return
    print("Product not found!")

def display_sales():
    if not products:
        print("No product records available!")
        return
    total_sales = 0
    highest = products[0]
    print("\n--- PRODUCT SALES REPORT ---")
    for product in products:
        revenue = product["quantity"] * product["price"]
        total_sales += revenue
        print("Product:", product["name"])
        print("Quantity sold:", product["quantity"])
        print("Revenue: Rs.", round(revenue, 2))
        if product["quantity"] > highest["quantity"]:
            highest = product
    print("Total sales: Rs.", round(total_sales, 2))
    print("Highest-selling product:", highest["name"])
    print("Quantity sold:", highest["quantity"])

while True:
    print("\n===== SALES DATA ANALYZER =====")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Display Sales Report")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_product()
    elif choice == "2":
        update_product()
    elif choice == "3":
        display_sales()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
