import sqlite3

def create_tables():
    # Connect to the SQLite database (or create it if it doesn't exist)
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    # Create the 'bands' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hometown TEXT NOT NULL
        );
    ''')

    # Create the 'venues' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            city TEXT NOT NULL
        );
    ''')

    # Create the 'concerts' table (which references both 'bands' and 'venues')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            band_id INTEGER,
            venue_id INTEGER,
            date TEXT NOT NULL,
            FOREIGN KEY (band_id) REFERENCES bands(id),
            FOREIGN KEY (venue_id) REFERENCES venues(id)
        );
    ''')

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
