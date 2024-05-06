from wrappers import input_error

@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if (name in contacts):
        return "Contact already exists"
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if (contacts[name]):
        contacts[name] = phone
        return "Contact updated."

@input_error
def get_contact(args: list, contacts: dict) -> str:
    name = args[0]
    return contacts[name]

@input_error
def get_all_contacts(contacts: dict) -> str:
    if not len(contacts):
        return "Contacts are empty"
    else:
        output = "Contacts:"
        for name, phone in contacts.items():
            output += f"\n{name}: {phone}"
        return output