import os
from model import comic
import comic_db

comic_database = None

def fileExists(filename):
    exists = os.path.isfile(filename)
    print("Checking if {filename} exists...{exists}".format(filename=filename, exists=exists))
    return exists

def get_record_from_user():
    universe = input("Universe: ")
    title = input("Title: ")
    serial = input("Serial: ")
    comic_database.add_record(universe, title, serial)

def menu():
    menu_items = [
        {
            "display": "Add new record",
            "function": get_record_from_user,
            "parameters": None
        },
        {
            "display": "Display all records",
            "function": print_records,
            "parameters": comic_database.find_all_records
        },
        {
            "display": "Exit",
            "function": exit,
            "parameters": None
        }
    ]

    while True:
        for index, item in enumerate(menu_items):
            print('{option}: {display}'.format(option=index+1, display=item["display"]))

        print()
        choice = input("Choice: ")
        choice = int(choice)
        choice = -1 if choice < 1 else choice - 1

        if choice < 0 or choice >= len(menu_items):
            pass
        else:
            if (menu_items[choice]["parameters"] is not None):

                print()
                print()

                menu_items[choice]["function"](
                    menu_items[choice]["parameters"]()
                )

                print()
                print()
            else:
                print()
                print()

                menu_items[choice]["function"]()

                print()
                print()

def null_func():
    pass

def print_records(records):

    print("{0:10s}{title}".format("Universe", title="Title"), end='\n\n')

    for record in records:
        id, universe, title, serial = list(record)
        print("{0:10s}{title}".format(universe, title=title))

def main():
    if not fileExists(comic_database.get_comic_database_filename()):
        comic_database.initializeDatabase()
    else:
        menu()

if __name__ == "__main__":
    comic_database = comic_db.ComicDatabase("comics.db")
    main()