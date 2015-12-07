import os
from model import comic
import comic_db

def fileExists(filename):
    exists = os.path.isfile(filename)
    print("Checking if {filename} exists...{exists}".format(filename=filename, exists=exists))
    return exists

def main():

    comic_database = comic_db.ComicDatabase("comics.db")

    if not fileExists(comic_database.get_comic_database_filename()):
        comic_database.initializeDatabase()
    else:
        print("Getting all records...")
        all_records = comic_database.find_all_records()

        for record in all_records:
            print(record)

        print()
        print("Getting all DC Universe records...")
        records = comic_database.find_by_universe(["DC"])

        for record in records:
            print(record)

        print()
        print("Getting all titles containing 'Superman'")
        records = comic_database.find_by_title(["%Superman%"])

        for record in records:
            print(record)

        print()
        print("Getting all serials with 0001...")
        records = comic_database.find_by_serial(["0001"])

        for record in records:
            print(record)

if __name__ == "__main__":
    main()