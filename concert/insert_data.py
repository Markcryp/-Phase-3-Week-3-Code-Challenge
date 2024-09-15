import sqlite3

def insert_data():
    # Connect to the SQLite database
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    # Insert sample data into 'bands' table
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Band A', 'New York')")
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Band B', 'Los Angeles')")

    # Insert sample data into 'venues' table
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Venue X', 'New York')")
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Venue Y', 'Los Angeles')")

    # Insert sample concerts into 'concerts' table
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-09-12')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 2, '2024-09-15')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 1, '2024-09-18')")

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    insert_data()
