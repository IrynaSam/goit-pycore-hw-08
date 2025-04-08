from handlers import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays, add_email, edit_email, add_address, edit_address
from parse import parse_input
from classes import AddressBook
import pickle

def save_data(book, addressbook):
    with open(addressbook, "wb") as file:
        pickle.dump(book, file)
        
def load_data(addressbook):
    try:
        with open(addressbook, "rb") as file:
            return  pickle.load(file)
            
    except FileNotFoundError:
        return AddressBook()
         
             
def main():
    book = load_data(addressbook="addressbook.pkl")
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        cmd, args = parse_input(user_input)

        if cmd in ["close", "exit"]:
            print("Good bye!")
            save_data(book, "addressbook.pkl")
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
        elif cmd == "add-email":
            print(add_email(args, book))
        elif cmd == "edit-email":
            print(edit_email(args, book))
        elif cmd == "add-address":
            print(add_address(args, book))
        elif cmd == "edit-address":
            print(edit_address(args, book))     
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()