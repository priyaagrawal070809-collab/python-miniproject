def contact_book():
    contact = {}
    while True:
        print("\n ---Welcome to the contact book!---")
        print("1. Add contact")
        print("2. search a contact")
        print("3. remove contact")
        print("4. Display all contact")
        print("5. quit")

        choice = input("Enter your choice:")

        if choice == "1":
            name = input("Enter a contact name to add in!:-").strip()
            if name in contact:
                print("already added!")
            else:
                phone = input("Enter the mobile number: ")
                email_id = input("enter an email: ")
                contact[name] = {
                    "phone": phone,
                    "email id": email_id
                }
                print(f"{name} has added!")
        
        elif choice == "2":
            name = input("Enter a contact name to search out!:-").strip()
            if name in contact:
                print("\n contact found!")
                print("phone",contact[name][phone])
                print("email_id",contact[name][email_id])
            else:
                print("contact not found!")
        elif choice == "3":
            name = input("Enter a contact name to search out!:-").strip()
            if name in contact:
                del contact[name]
                print(f"{name} has removed!")
            else:
                print("not found!")
        elif choice == "4":
            if not contact:
                print("no contact found!")
            else:
                print("\n---contacts---")
                for name,details in contact.item():
                    print(f"\nName : {name}")
                    print(f"Phone: {details['phone']}")
                    print(f"Email: {details['email']}")
        elif choice == "5":
            print("ending!")
            break
        else:
            print("invalid choice!")
    return contact
print(contact_book())
