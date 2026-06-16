
def bill_splitter(num):
    menu = {
        "1": ("white sauce pasta", 150),
        "2": ("grilled cheese sandwich", 90),
        "3": ("red sauce pasta", 120),
        "4": ("steam veg dumplings", 35),
        "5": ("peri peri fries", 50),
        "6": ("cheedar cheese fries", 70),
        "7": ("veg cheese pizza",210),
        "8": ("veg burger", 55),
        "9": ("veg kaathi roll",75),
        "10": ("oreo shake",90),
    }
    ordered_items = []
    total = 0.0

    while True:
        print("=== Display the menu ===")
        for key, (name, price) in menu.items():#.items = list of tuples where each tuple is (key, value) and value is also a tuple (name, price)
            print(f"{key}. {name} : {price}/-")
#here we can not use total+=price bcoz total bill is inflating before the user even chooses anything.
        choice = input("Enter the item number or 'done' to finish: ")
        if choice.lower() == 'done':
            break
        if choice in menu:
            item_name, item_price = menu[choice]
            ordered_items.append((item_name, item_price))
            total += item_price
            print(f"Added {item_name} for {item_price}/-. Current total: {total}/-")
        else:
            print("Invalid choice!")

    if not ordered_items:
        print("No items ordered.")
        return 0.0
    
    tip = total * 0.10
    share = total / num
    s_tip = tip / num
    result = share + s_tip
    print("\n" + "="*20)
    print("    BILL RECEIPT")
    print("\n" + "="*20)
    
    for items, price in ordered_items:
        print(f"{items:<10} {price}/-")
    
    print(f"\n total bill: {total}/-")
    print(f" tip(10%): {tip}/-")
    print(f" bill shared: {share}/-")
    print(f" tip shared: {s_tip}/-")
    print(f"\n amount each person should pay: {result}/-")
    return result
num = int(input("Enter number of people: "))
print("The amount each person should pay is:", bill_splitter(num))
    