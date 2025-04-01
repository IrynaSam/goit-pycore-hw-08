from handlers import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from parse import parse_input
from classes import AddressBook

def main():
    book = AddressBook()
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        cmd, args = parse_input(user_input)

        if cmd in ["close", "exit"]:
            print("Good bye!")
            break

        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add_contact(args, book))
        elif cmd == "change":
            print(change_contact(args, book))  
        elif cmd == "phone":
            print(show_phone(args, book))
        elif cmd == "all":
            print(show_all(book))
        elif cmd == "add-birthday":
            print(add_birthday(args, book))
        elif cmd == "show-birthday":
            print(show_birthday(args, book))
        elif cmd == "birthdays":
            print(birthdays(args, book))  
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()