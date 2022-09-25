from typing import Union

import requests


class BookAPI:
    BOOK_API_URL = "https://www.googleapis.com/books/v1/volumes"

    def __init__(self):
        ...

    def fetch_book_api(self, search: Union[None, str] = None):

        params = {
            'q': search
        }
        result = dict(requests.get(self.BOOK_API_URL, params=params).json())
        print(result)
        if not result.get('items'):
            return None

        if not result.get('items')[0]['volumeInfo']:
            return None

        return result
