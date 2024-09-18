import sqlite3

class Band:
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

    # Fetch all concerts associated with the band
    def concerts(self):
        connection = sqlite3.connect('concerts.db')
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM concerts WHERE band_id = ?", (self.id,))
            concerts = cursor.fetchall()
        finally:
            connection.close()

        return concerts

    # Fetch all distinct venues where the band has performed
    def venues(self):
        connection = sqlite3.connect('concerts.db')
        try:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT DISTINCT venues.*
                FROM concerts
                JOIN venues ON concerts.venue_id = venues.id
                WHERE concerts.band_id = ?
            """, (self.id,))
            venues = cursor.fetchall()
        finally:
            connection.close()

        return venues

    # Play a concert at a specific venue on a given date
    def play_in_venue(self, venue_id, date):
        connection = sqlite3.connect('concerts.db')
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO concerts (band_id, venue_id, date)
                VALUES (?, ?, ?)
            """, (self.id, venue_id, date))
            connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
