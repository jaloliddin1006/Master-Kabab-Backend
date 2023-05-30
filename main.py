from geopy.geocoders import Nominatim
def manzil(latitude,longitude):
    geolocator = Nominatim(user_agent="Behzod")
    location = geolocator.reverse(f'{latitude},{longitude}')
    return location.address