import requests

from typing import Optional
from pprint import pprint

from api.books.parser import BooksMetaParserAPI


class BooksMetadataAPI:
    def __init__(self) -> None:
        self.search_url = "https://openlibrary.org/search.json?q={}"
        self.book_url = "https://openlibrary.org/books/{}.json"
        self.meta_parser = BooksMetaParserAPI()

    def search_book(self, book_name: str, translate_title: bool = False) -> Optional[dict]:
        if translate_title:
            search_book_name = self.meta_parser.get_english_book_name(portuguese_title=book_name)
        else:
            search_book_name = str(book_name)

        search_url_fmt = self.search_url.format(search_book_name)

        response = requests.get(url=search_url_fmt)
        if response.status_code != 200 and not translate_title:
            return self.search_book(book_name=search_book_name, translate_title=True)
        elif response.status_code != 200 and translate_title:
            return None

        book_data = response.json().get("docs", None)
        if book_data is None:
            return None

        return book_data[0]

    def get_book_metadata(self, book_name: str) -> Optional[dict]:
        book_info = self.search_book(book_name=book_name)
        if book_info is None:
            return None

        work_id = book_info["key"].split("/")[-1]
        response = requests.get(url=self.book_url.format(work_id))
        if response.status_code != 200:
            return None

        book_metadata = response.json()

        parsed_meta = self.meta_parser.parse_metadata(book_meta=book_metadata, book_info=book_info)
        return parsed_meta


if __name__ == "__main__":
    meta_api = BooksMetadataAPI()
    search_term = "De gênio a louco, todo mundo tem um pouco"

    book_meta = meta_api.get_book_metadata(book_name=search_term)
    pprint(book_meta, sort_dicts=False)
