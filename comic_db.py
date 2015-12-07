import sqlite3

class ComicDatabase(object):

    connection = None # null object

    def __init__(self, comic_db_filename):
        self.comic_db_filename = comic_db_filename

    def get_comic_database_filename(self):
        return self.comic_db_filename

    def initializeDatabase(self):
        connection = sqlite3.connect(self.comic_db_filename) # should create database if it doesn't exist
        try:
            print("Attempting to create database...")
            connection.execute('''
                                CREATE TABLE IF NOT EXISTS comics (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    universe varchar(20) NOT NULL,
                                    title varchar(255) NOT NULL,
                                    serial varchar(50) NOT NULL
                                )
                                ''')

            values = [("DC", "Superman (The New 52)", "0001"),
                      ("DC", "Batman (The New 52)", "0001"),
                      ("Marvel", "X-Men", "0001")]

            connection.executemany('''
                                INSERT INTO comics (universe, title, serial) VALUES (?,?,?)
                                ''', values)
            connection.commit()
            connection.close()
            print("Database is created!")
        except sqlite3.Error:
            print("SQLite3 error. Exiting.")
        except FileNotFoundError:
            print("{filename} not found and could not be created. Exiting.".format(filename=self.comic_db_filename))

    def add_record(self, universe, title, serial):
        try:
            connection = sqlite3.connect(self.comic_db_filename)

            record = [universe, title, serial]
            connection.execute('''
                        INSERT INTO comics (universe, title, serial) VALUES (?,?,?)
                        ''', record)

            connection.commit()
            connection.close()
            print("{record} was created!".format(record=record))
        except sqlite3.Error as er:
            print('SQL Record Failed: ', er.message)

    def find_all_records(self):
        connection = sqlite3.connect(self.comic_db_filename)
        c = connection.cursor()

        c.execute("SELECT * FROM comics")

        tmp = c.fetchall()
        connection.close()

        return tmp

    def find_by_universe(self, universe):
        connection = sqlite3.connect(self.comic_db_filename)
        c = connection.cursor()

        c.execute("SELECT * FROM comics WHERE universe = ?", universe)

        tmp = c.fetchall()
        connection.close()

        return tmp

    def find_by_title(self, title):
        connection = sqlite3.connect(self.comic_db_filename)
        c = connection.cursor()

        c.execute("SELECT * FROM comics WHERE title LIKE ?", title)

        tmp = c.fetchall()
        connection.close()

        return tmp

    def find_by_serial(self, serial):
        connection = sqlite3.connect(self.comic_db_filename)
        c = connection.cursor()

        c.execute("SELECT * FROM comics WHERE serial = ?", serial)

        tmp = c.fetchall()
        connection.close()

        return tmp
