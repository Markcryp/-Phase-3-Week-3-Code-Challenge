from concert.band import Band
from concert.venue import Venue
from concert.concert import Concert

def test_setup():
    # Create and save a Band
    band_1 = Band(None, 'Rockas', 'New York')
    band_1.save()

    # Create and save a Venue
    venue_1 = Venue(None, 'Bullet', 'Los Angeles')
    venue_1.save()

    # Create a Concert
    band_1.play_in_venue(venue_1.id, '2024-09-01')

    # Test methods
    print(band_1.concerts())
    print(band_1.venues())
    print(band_1.all_introductions())
    print(Band.most_performances())
    
    venue_1_concert = venue_1.concert_on('2024-09-01')
    print(venue_1_concert)
    print(venue_1.most_frequent_band())
    
    concert = Concert(1, band_1.id, venue_1.id, '2024-09-01')
    print(concert.hometown_show())
    print(concert.introduction())

if __name__ == '_main_':
    test_setup()

