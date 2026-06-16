import datetime
def unit_convert():
    history = []
    while True:
        print("\n ===unit conversion toolpanel===")
        print("1. length")
        print("2. weight")
        print("3. temperatur")
        print("4. history")
        print("5. quit")
        choice = input("Enter your choice among the available units:")
        if choice == "1":
            print("\n ===length conversion===")
            print("1. kilometer to miles")
            print("2. miles to kilometer")
            l_choice = input("Enter your choice for length conversion:")
            if l_choice == "1":
                km = float(input("Enter a distance in km: "))
                miles = km*0.62
                print(f"{km} to miles: {miles}")
                history.append(miles)
            elif l_choice == "2":
                miles = float(input("Enter a distance in miles: "))
                km = miles/0.62
                print(f"{miles} to km is: {km}")
                history.append(km)
        elif choice == "2":
            print("\n ===weight conversion===")
            print("1. kilogram to lbs")
            print("2. lbs to kilogram")
            w_choice = input("Enter your choice for weight conversion:")
            if w_choice == "1":
                kg = float(input("Enter a weight in kg: "))
                lbs = kg*2.20462
                print(f"{kg} to lbs is: {lbs}")
                history.append(lbs)
            elif w_choice == "2":
                lbs = float(input("Enter a weight in lbs: "))
                kg = lbs/2.20462
                print(f"{lbs} to kg is: {kg}")
                history.append(kg)
        elif choice == "3":
            print("\n ===temperature conversion===")
            print("1. celcius to fahrenheit")
            print("2. fahrenheit to celcius")
            t_choice = input("Enter your choice for temperature conversion:")
            if t_choice == "1":
                c = float(input("Enter a temperature in celcius: "))
                f = (c*9/5) + 32
                print(f"{c} to fahrenheit is: {f}")
                history.append(f)
            elif t_choice == "2":
                f = float(input("Enter a temperature in fahrenheit: "))
                c = (f-32)*5/9
                print(f"{f} to celcius is: {c}")
                history.append(c)
        elif choice == "4":
            print("\n ===conversion history===")
            for record in history:
                if record!=0:
                    print(record)
                else:
                    print("no history has been recorded!")
        elif choice == "5":
            print("Exiting the unit conversion tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    return history

print(unit_convert())

