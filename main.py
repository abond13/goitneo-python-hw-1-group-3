"""
    Домашнє завдання №1
    Завдання №2
"""
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def print_help():
    return "Available commands:\n" + \
           "\tadd [name] [phone]\n" + \
           "\tchange [name] [phone]\n" + \
           "\tphone [name]\n" + \
           "\tall\n" + \
           "\texit"


def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    return "[ERROR] Expected command: add [name] [phone]"

def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        return "[ERROR] No such contact."
    return "[ERROR] Expected command: change [name] [phone]"

def phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        return "[ERROR] No such contact."
    return "[ERROR] Expected command: phone [name]"

def show_all(contacts):
    res = ''
    for name, phone in contacts.items():
        res += name + " : " + phone + "\n"
    return res

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)
        else:
            continue
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "help":
            print(print_help())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
