from decorators import input_error
from classes import AddressBook

@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Потрібно ввести ім`я та телефон")

    name, phone = args[0], args[1]
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        from classes import Record  
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)
    return message
@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return "Введіть ім`я та дату народження у форматі: add-birthday Імʼя DD.MM.YYYY"
    
    name, birthday_str = args[0], args[1]

    record = book.find(name)
    if record is None:
        return f"Контакт з іменем '{name}' не знайдено."

    try:
        record.add_birthday(birthday_str)
        return f"День народження для {name} додано: {birthday_str}"
    except ValueError as e:
        return f" {str(e)}"
    
@input_error
def show_birthday(args, book: AddressBook):
    if len(args) < 1:
        return "Введіть ім`я: show-birthday Ім`я"

    name = args[0]
    record = book.find(name)

    if record is None:
        return f"Контакт з іменем '{name}' не знайдено."

    if record.birthday is None:
        return f"У контакту '{name}' не вказано день народження."

    birthday_str = record.birthday.value.strftime("%d.%m.%Y")
    return f"День народження {name}: {birthday_str}"

@input_error
def birthdays(args, book: AddressBook):
    days = 7 # якщо введено команду birthdays без к-сті днів виведена на імениники тижні
    
    if args:
        try:
            days = int(args[0])
        except ValueError:
            return "Будь ласка, введіть число: birthdays 10"
            
    result = book.get_upcoming_birthdays(days)

    if not any(result.values()):
        return f"Немає іменинників протягом {days} днів."

    lines =  [f"Привітання на наступні {days} днів:"]
    for day, names in result.items():
        if names:
            lines.append(f"{day}: {', '.join(names)}")

    return "\n".join(lines).strip()


@input_error
def change_contact(args, book: AddressBook):
    if len(args)<2:
        raise ValueError
    name, old_phone, new_phone = args[0], args[1], args[2]
    record = book.find(name)

    if record is None:
        raise KeyError("Контакт не знайдено")

    updated = record.edit_phone(old_phone, new_phone)
    if updated:
        return "Номер змінено."
    return "Старий номер не знайдено."
@input_error
def show_phone(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("Введіть ім`я")

    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError("Контакт не знайдено")

    phones = ", ".join(p.value for p in record.phones)
    return f"Телефони {name}: {phones}"

@input_error
def show_all(book):
    if not book.data:
        return "Контактів поки немає."

    lines = ["Контакти:", "-" * 30]

    for record in book.data.values():
        lines.append(f"{record.name.value}")
        
        # телефони
        phones = ", ".join(p.value for p in record.phones)
        lines.append(f"Телефони: {phones if phones else 'немає'}")

        # день народження
        if record.birthday:
            birthday = record.birthday.value.strftime("%d.%m.%Y")
            lines.append(f"День народження: {birthday}")
        else:
            lines.append("День народження: не вказано")
        
        # email
        if hasattr(record, "email") and record.email:
            lines.append(f"Email: {record.email.value}")
        else:
            lines.append("Email: не вказано")
        
        # адреса
        if hasattr(record, "address") and record.address:
            lines.append(f"Адреса: {record.address.value}")
        else:
            lines.append("Адреса: не вказано")
        
        lines.append("") 

    return "\n".join(lines).strip()

@input_error
def add_email(args, book: AddressBook):
    if len(args)<2:
        return "Введіть ім'я та email: add-email Ім'я email@example.com"
    name, email = args[0], args[1]
    record = book.find(name)
    
    if record is None:
        return f"Контакт з іменем '{name}' не знайдено."
    
    record.add_email(email)
    return f"Email для {name} додано: {email}"

@input_error
def edit_email(args, book: AddressBook):
    if len(args) <2:
        return "Введіть ім'я та новий email: edit-email Ім'я new_email@example.com"
    
    name, new_email = args[0], args[1]
    record = book.find(name)
    
    if record is None:
        return f"Контакт з іменем '{name}' не знайдено."
    
    record.edit_email(new_email)
    return f"Email для {name} змінено на: {new_email}"

@input_error
def add_address(args, book: AddressBook):
    if len(args) <2:
        return "Введіть ім'я та адресу: add-address Ім'я Адреса"
    
    name = args[0]
    address_str = " ".join(args[1:])
    record = book.find(name)
    
    if record is None:
        return f"Контакт з іменем '{name}' не знайдено."
    
    record.add_address(address_str)
    return f"Адреса для {name} додана: {address_str}"

@input_error
def edit_address(args, book: AddressBook):
    
    
    if len(args) <2:
        return "Введіть ім'я та нову адресу: edit-address Ім'я Нова адреса" 
    
    name = args[0]
    new_address = " ".join(args[1:])
    record = book.find(name)
    
    if record is None:
        return f"Контакт з іменем '{name}' не знайдено."
    
    record.edit_address(new_address)
    return f"Адреса для {name} змінена на: {new_address}" 
    