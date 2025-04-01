from collections import UserDict
from datetime import datetime as dtdt
from datetime import timedelta as dttd

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            self.value = value
        else:
            raise ValueError("Номер має складатися з 10 цифр")
        
class Birthday(Field):
    def __init__(self, value):
        try:
            date_obj = dtdt.strptime(value, "%d.%m.%Y")
            super().__init__(date_obj)
        except ValueError:
            raise ValueError("Невірний формат дати. Використовуй DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i
        return None
    
    def edit_phone(self, old_phone, new_phone):
        for i in self.phones:
            if i.value == old_phone:
                i.value = new_phone
                return i
        return None
    
    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
                
    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)
        
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        
    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None 
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def get_upcoming_birthdays(self):
        today = dtdt.today().date()
        next_week = today + dttd(days=7)
        birthdays_per_day = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": []
        } 
        for record in self.data.values():
            if record.birthday == None:
                continue
            bday = record.birthday.value
            bday_this_year = bday.replace(year=today.year)
            bday_this_year = bday_this_year.date()
            if bday_this_year < today:
                bday_this_year = bday_this_year.replace(year=today.year + 1)

            if today <= bday_this_year <= next_week:
                weekday = bday_this_year.strftime("%A")
                if weekday in ["Saturday", "Sunday"]:
                    weekday = "Monday"
                birthdays_per_day[weekday].append(record.name.value)
           
        
        
        return birthdays_per_day

                    

            
        
        

