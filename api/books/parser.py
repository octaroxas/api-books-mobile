from typing import List, Optional

from translate import Translator


class BooksMetaParserAPI:
    def __init__(self) -> None:
        self.translator = Translator(
            to_lang="pt"
        )

    def _parse_title(self, book_metadata: dict) -> Optional[str]:
        target_key = "title"

        original_title = book_metadata.get(target_key, None)
        if original_title is None:
            return None

        translated_title = self.translator.translate(text=original_title)
        return translated_title

    @staticmethod
    def _shorten_abstract(book_abstract: str, character_limit: int = 255) -> str:
        abstract_parts = book_abstract.split(".")

        shortened_abstract = ""
        for part in abstract_parts:
            if (len(shortened_abstract) + len(part)) > character_limit:
                break

            shortened_abstract += part

        return shortened_abstract

    def _parse_abstract(self, book_metadata: dict) -> Optional[str]:
        target_key = "description"

        original_abstract = book_metadata.get(target_key, None)
        if original_abstract is None:
            return None

        shortened_abstract = self._shorten_abstract(book_abstract=original_abstract)
        translated_abstract = self.translator.translate(text=shortened_abstract)
        return translated_abstract

    def _parse_subjects(self, book_metadata: dict) -> Optional[List[str]]:
        target_key = "subjects"

        original_subjects = book_metadata.get(target_key, None)
        if original_subjects is None:
            return None

        shortened_subjects = original_subjects[:5]
        translated_subjects = [self.translator.translate(text=subject) for subject in shortened_subjects]
        return translated_subjects

    @staticmethod
    def _parse_isbn(book_info_data: dict) -> Optional[str]:
        target_key = "isbn"

        book_isbn_list = book_info_data.get(target_key, None)
        if book_isbn_list is None:
            return None

        for isbn in book_isbn_list:
            if str(isbn).isdigit():
                return str(isbn)

        return None

    @staticmethod
    def _parse_first_published_year(book_info_data: dict) -> str:
        target_key = "first_publish_year"

        published_year = book_info_data[target_key]
        return str(published_year)

    @staticmethod
    def _parse_authors(book_info_data: dict) -> List[str]:
        target_key = "author_name"

        authors = book_info_data[target_key]
        return authors

    @staticmethod
    def _parse_number_of_pages(book_info_data: dict) -> int:
        target_key = "number_of_pages_median"

        number_of_pages = int(book_info_data[target_key])
        return number_of_pages

    @staticmethod
    def _parse_book_cover_id(book_info_data: dict) -> Optional[int]:
        target_key = "cover_i"

        book_cover_id = book_info_data.get(target_key, None)
        if book_cover_id is None:
            return None

        cover_id = int(book_cover_id)
        return cover_id

    @staticmethod
    def get_english_book_name(portuguese_title: str) -> str:
        eng_translator = Translator(to_lang="en", from_lang="pt")

        eng_title = eng_translator.translate(text=portuguese_title)
        return eng_title

    def parse_metadata(self, book_meta: dict, book_info: dict) -> dict:
        parsed_metadata = {
            "title": self._parse_title(book_metadata=book_meta),
            "abstract": self._parse_abstract(book_metadata=book_meta),
            "subjects": self._parse_subjects(book_metadata=book_meta),
            "isbn": self._parse_isbn(book_info_data=book_info),
            "year": self._parse_first_published_year(book_info_data=book_info),
            "authors": self._parse_authors(book_info_data=book_info),
            "pages": self._parse_number_of_pages(book_info_data=book_info),
            "cover_id": self._parse_book_cover_id(book_info_data=book_info)
        }

        return parsed_metadata
