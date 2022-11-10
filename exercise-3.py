address_book = {}


def store_info(vals):
    keys = ['name', 'address', 'city']
    new_dict = {keys[i]: vals[i] for i in range(len(keys))}
    address_book[new_dict['name']] = new_dict


def get_info():
    running = True
    while running:

        asking = True
        while asking:
            valid_responses = ['a', 'v', 'q']
            user_input = input(
                "Would you like to add another entry, view the entries, or quit? (A)dd / (V)iew / (Q)uit:  ")
            if user_input.lower() not in valid_responses:
                print(
                    f"{user_input} is not a valid input. Please select (A)dd, (V)iew, or (Q)uit: ")
            else:
                asking = False

        if user_input.lower() == 'a':
            store_info([input("Name: "), input("Address: "), input("City: ")])

        if user_input.lower() == 'v':
            if not address_book:
                print("There are no entries in the address book.")
            else:
                print(address_book)

        if user_input.lower() == 'q':
            running = False
            print("Quit successfully")
            break


get_info()
