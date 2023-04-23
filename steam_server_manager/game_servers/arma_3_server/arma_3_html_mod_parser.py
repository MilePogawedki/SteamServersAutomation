from typing import List
from bs4 import BeautifulSoup, Tag

from steam_server_manager.common.workshopmod import WorkshopMod


class WrongFileError(Exception):
    ...


class Arma3HtmlModParser:
    def __init__(self, html_raw: str) -> None:
        self.html_raw = html_raw
        self._mods_list: List[WorkshopMod] = []
        self._parse()

    def get_mods_list(self) -> List[WorkshopMod]:
        return self._mods_list

    def _parse(self):
        soup = BeautifulSoup(self.html_raw, "html.parser")
        if soup.title.text != "Arma 3":
            raise WrongFileError("Bad html file")
        html_mods = soup.find_all("tr")
        self._mods_list = [
            WorkshopMod(
                mod_id=self._get_mod_id_from_row(html_mod_row),
                mod_name=self._get_mod_name_from_row(html_mod_row),
            )
            for html_mod_row in html_mods
        ]

    @staticmethod
    def _get_mod_id_from_row(html_row: Tag) -> int:
        return Arma3HtmlModParser._get_id_from_href(
            html_row.find_next("a").get("href")
        )

    @staticmethod
    def _get_id_from_href(href: str) -> int:
        return int(href.split("?id=")[-1])

    @staticmethod
    def _get_mod_name_from_row(html_row: Tag) -> str:
        return html_row.find_next("td").text.lower()
