import sqlite3

class Concert:
    def __init__(self, id, band_id, venue_id, date):
        """Initialize a Concert instance with id, band_id, venue_id, and date"""
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @classmethod
    def get_by_id(cls, concert_id):
        """
        Fetch a Concert instance by its ID from the database.
        :param concert_id: The ID of the concert
        :return: Concert instance if found, otherwise None
        """
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        
        # Fetch the concert record by ID
        cursor.execute("SELECT * FROM concerts WHERE id = ?", (concert_id,))
        row = cursor.fetchone()  # Fetch a single row
        connection.close()

        if row:
            # Return a Concert instance if found
            return cls(row[0], row[1], row[2], row[3])
        else:
            return None

    def band(self):
        """
        Fetch the band associated with this concert from the database.
        :return: Band record as a tuple (id, name, hometown), otherwise None
        """
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        
        # Fetch the band by band_id
        cursor.execute("SELECT * FROM bands WHERE id = ?", (self.band_id,))
        band = cursor.fetchone()  # Fetch the band record
        connection.close()

        return band

    def venue(self):
        """
        Fetch the venue associated with this concert from the database.
        :return: Venue record as a tuple (id, title, city), otherwise None
        """
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        
        # Fetch the venue by venue_id
        cursor.execute("SELECT * FROM venues WHERE id = ?", (self.venue_id,))
        venue = cursor.fetchone()  # Fetch the venue record
        connection.close()

        return venue

    def hometown_show(self):
        """
        Check if this concert is a hometown show, i.e., if the band's hometown matches the venue's city.
        :return: True if it's a hometown show, otherwise False
        """
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        
        # Fetch data to compare band's hometown and venue's city
        cursor.execute("""
            SELECT concerts.id, bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        """, (self.id,))
        
        row = cursor.fetchone()  # Fetch the result of the join query
        connection.close()

        # If the band's hometown matches the venue's city, it's a hometown show
        if row and row[1] == row[2]:
            return True
        else:
            return False
