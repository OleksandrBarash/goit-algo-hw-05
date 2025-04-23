# Бот-помічник з обробкою помилок через декоратор
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all(args, contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def parse_command(command_str):
    parts = command_str.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main():
    print("Welcome to the assistant bot!")
    while True:
        command_str = input("Enter a command: ")
        if command_str.lower() in ["exit", "close", "good bye"]:
            print("Good bye!")
            break

        command, args = parse_command(command_str)

        if command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()