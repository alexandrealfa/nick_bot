import requests
from datetime import date as dt

from config import NASA_API_KEY


class NasaAPI:
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    URL_EARTH = "https://api.nasa.gov/planetary/earth/imagery"

    def __init__(self):
        ...

    def fetchAPOD(self, date=None, is_hd=True):
        if not date:
            date = dt.today()

        params = {
            'api_key': NASA_API_KEY,
            'date': date,
            'hd': is_hd
        }

        return dict(requests.get(self.URL_APOD, params=params).json())

    def featchEarth(self):
        ...
