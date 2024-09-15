import sqlite3

class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @staticmethod
    def get_by_id(concert_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM concerts WHERE id = ?", (concert_id,))
        row = cursor.fetchone()
        connection.close()

        if row:
            return Concert(row[0], row[1], row[2], row[3])
        else:
            return None

    def band(self):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM bands WHERE id = ?", (self.band_id,))
        band = cursor.fetchone()
        connection.close()

        return band

    def venue(self):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM venues WHERE id = ?", (self.venue_id,))
        venue = cursor.fetchone()
        connection.close()

        return venue

    def hometown_show(self):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT concerts.id, bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        """, (self.id,))
        row = cursor.fetchone()
        connection.close()

        if row and row[1] == row[2]:
            return True
        else:
            return False
