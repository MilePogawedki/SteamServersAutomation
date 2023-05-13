from typing import Dict
from bs4 import BeautifulSoup, Tag

from steam_server_manager.common.workshopmod import WorkshopMod


class WrongFileError(Exception):
    ...


class Arma3HtmlModParser:
    def __init__(self, html_raw: str) -> None:
        self.html_raw = html_raw
        self._mods_list: Dict[int, WorkshopMod] = {}
        self._parse()

    def get_mods_list(self) -> Dict[int, WorkshopMod]:
        return self._mods_list

    def _parse(self) -> None:
        soup = BeautifulSoup(self.html_raw, "html.parser")
        if soup.title and soup.title.text != "Arma 3":
            raise WrongFileError("Bad html file")
        html_mods = soup.find_all("tr")
        self._mods_list = {
            mod_id: WorkshopMod(
                mod_id=mod_id,
                mod_name=self._get_mod_name_from_row(html_mod_row),
            )
            for html_mod_row in html_mods
            if (mod_id := self._get_mod_id_from_row(html_mod_row))
        }

    @staticmethod
    def _get_mod_id_from_row(html_row: Tag) -> int:
        if (
            (mod_link := html_row.find_next("a"))
            and isinstance(mod_link, Tag)
            and (href := mod_link.get("href"))
            and isinstance(href, str)
        ):
            return Arma3HtmlModParser._get_id_from_href(href)
        raise Exception("Broken Arma3 HTML file")

    @staticmethod
    def _get_id_from_href(href: str) -> int:
        return int(href.split("?id=")[-1])

    @staticmethod
    def _get_mod_name_from_row(html_row: Tag) -> str:
        if row := html_row.find_next("td"):
            return row.text.lower()
        raise Exception("Broken Arma3 HTML file")
