import sqlite3

class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    # Fetch all concerts associated with this venue
    def concerts(self):
        connection = sqlite3.connect('concerts.db')
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM concerts WHERE venue_id = ?", (self.id,))
            concerts = cursor.fetchall()  # Fetch all matching records
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            concerts = []
        finally:
            connection.close()  # Ensure connection is closed even if an error occurs

        return concerts

    # Fetch all distinct bands that have performed at this venue
    def bands(self):
        connection = sqlite3.connect('concerts.db')
        try:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT DISTINCT bands.*
                FROM concerts
                JOIN bands ON concerts.band_id = bands.id
                WHERE concerts.venue_id = ?
            """, (self.id,))
            bands = cursor.fetchall()  # Fetch all matching records
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            bands = []
        finally:
            connection.close()  # Ensure connection is closed even if an error occurs

        return bands
