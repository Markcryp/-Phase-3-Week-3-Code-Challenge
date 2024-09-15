import sqlite3

# Connect to the SQLite database (it will create the file if it doesn't exist)
connection = sqlite3.connect('concerts.db')
cursor = connection.cursor()

# Create the 'bands' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS bands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL
)
''')

# Create the 'venues' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    city TEXT NOT NULL
)
''')

# Create the 'concerts' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS concerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    band_id INTEGER,
    venue_id INTEGER,
    date TEXT,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (venue_id) REFERENCES venues(id)
)
''')

# Insert data into 'bands' table
bands_data = [
    ('Band A', 'New York'),
    ('Band B', 'Los Angeles'),
    ('Band C', 'Chicago')
]

cursor.executemany('INSERT INTO bands (name, hometown) VALUES (?, ?)', bands_data)

# Insert data into 'venues' table
venues_data = [
    ('Venue A', 'New York'),
    ('Venue B', 'Los Angeles'),
    ('Venue C', 'Chicago')
]

cursor.executemany('INSERT INTO venues (title, city) VALUES (?, ?)', venues_data)

# Insert data into 'concerts' table
concerts_data = [
    (1, 1, '2024-09-01'),  # Band A plays at Venue A on 2024-09-01
    (2, 2, '2024-09-02'),  # Band B plays at Venue B on 2024-09-02
    (3, 3, '2024-09-03')   # Band C plays at Venue C on 2024-09-03
]

cursor.executemany('INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)', concerts_data)

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Tables created and data inserted successfully.")
