import re
from datetime import datetime

# Superclass
class Reminders:
    def __init__(self, person_or_organization, location, date, time):
        self.person_or_organization = person_or_organization
        self.location = location
        self.date = date
        self.time = time

    def info(self):
        return f"{self.person_or_organization}, {self.location}, {self.date}, {self.time}"

    def date_parsed(self):
        try:
            date_obj = datetime.strptime(self.date, "%d/%m/%Y")
            return date_obj
        except (ValueError, TypeError):
            return datetime.max

# Subclass
class UserEntry(Reminders):
    def __init__(self):
        super().__init__("Empty", "Empty", "01/01/1900", "00:00")
        self.entries = []
        self.entry_id_counter = 0

    def entry_date(self):
        print("Please enter the date (e.g., '27 08 1993', '27-08-1993', '27.08.1993', '27_08_1993').")
        date_entry = input("Date: ")

        # Define regular expressions to match various date formats
        date_patterns = [
            r'(\d{2})[ -./_](\d{2})[ -./_](\d{4})',
            # Add more patterns for other formats as needed
        ]

        date_obj = None
        for pattern in date_patterns:
            match = re.match(pattern, date_entry)
            if match:
                day, month, year = match.groups()
                date_str = f"{day}/{month}/{year}"
                try:
                    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
                    break
                except ValueError:
                    pass

        if date_obj is None:
            print("Invalid date format. Please enter the date in a valid format.")
            return

        time = input("Time: ")
        person_or_organization = input("Person or Organization: ")
        location = input("Location: ")

        entry = Reminders(person_or_organization, location, date_obj.strftime("%d/%m/%Y"), time)
        self.entries.append(entry)
        self.entry_id_counter += 1
        print("Entry successfully saved!")

    def delete_entry(self, person=None, date=None):
        if person is not None:
            entries = [entry for entry in self.entries if person != entry.person_or_organization]
        elif date is not None:
            entries = [entry for entry in self.entries if date != entry.date]
        else:
            print("Please enter the name or date of the entry you want to delete.")
            return

        if len(entries) == len(self.entries):
            print("This entry could not be found.")
        else:
            self.entries = entries
            print("Entry successfully deleted!")

    def info(self):
        sorted_entries = sorted(self.entries, key=lambda x: x.date_parsed() or datetime.max)

        print("Recorded events:")
        for index, entry in enumerate(sorted_entries):
            print(f"{index}. {entry.info()}")

    def edit_entry(self):
        try:
            entry_id = int(input("Enter the ID of the entry you want to edit: "))
            if entry_id < len(self.entries):
                entry = self.entries[entry_id]
                person_or_organization = input("Person or Organization: ")
                location = input("Location: ")
                date = input("Date (Day Month Year): ")
                time = input("Time: ")

                entry.person_or_organization = person_or_organization
                entry.location = location
                entry.date = date
                entry.time = time
                print("Entry successfully updated!")
            else:
                print("Invalid entry ID.")
        except ValueError:
            print("Invalid entry ID.")

# Main program
print("Personal Agenda")
user_entry = UserEntry()

while True:
    print("Available actions:")
    print("1. Add an Entry")
    print("2. Delete an Entry (by Person or Date)")
    print("3. Show Entries")
    print("4. Edit an Entry")
    print("5. Type 'q' to exit.")

    choice = input("What would you like to do? : ")

    if choice.lower() == 'q':
        break

    if choice == "1":
        user_entry.entry_date()

    elif choice == "2":
        person_to_delete = input("Enter the name or organization you want to delete: ")
        date_to_delete = input("Enter the date (Day Month Year) you want to delete: ")
        user_entry.delete_entry(person_to_delete, date_to_delete)

    elif choice == "3":
        user_entry.info()

    elif choice == "4":
        user_entry.edit_entry()
