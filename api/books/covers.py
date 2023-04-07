import requests

from typing import Union, Optional


class BooksCoverAPI:
    def __init__(self) -> None:
        self.ext_url = "https://covers.openlibrary.org/b/{}/{}-{}.jpg"
        self.cover_size = "L"
        self.meta_type = "isbn"

    def set_cover_size(self, cover_size: str = "L") -> None:
        accepted_cover_sizes = ["S", "M", "L"]
        if cover_size not in accepted_cover_sizes:
            raise ValueError(f"The informed Book Cover Size ({cover_size}) is invalid.")

        self.cover_size = cover_size

    def set_metadata_type(self, meta_type: str = "isbn") -> None:
        accepted_meta_types = ["ISBN", "OCLC", "LCCN", "OLID", "ID"]
        if meta_type not in accepted_meta_types:
            raise ValueError(f"The informed Book MetaID Type ({meta_type}) is invalid.")

        self.meta_type = meta_type

    def get_book_cover(self, book_id: Union[str, int]) -> Optional[bytes]:
        cover_url = self.ext_url.format(self.meta_type, book_id, self.cover_size)

        response = requests.get(url=cover_url, params={"default": False})
        if response.status_code != 200:
            return None

        return response.content
