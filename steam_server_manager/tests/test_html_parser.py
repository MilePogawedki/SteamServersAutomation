import os

from steam_server_manager.game_servers.arma_3_server.arma_3_html_mod_parser import Arma3HtmlModParser


class TestHtmlModParser:
    def test_parsing(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, "test_a3mods.html"), "r") as file:
            raw_html = file.read()
        parser = Arma3HtmlModParser(raw_html)
        id_list = [
            workshop_mod.mod_id
            for workshop_mod in parser.get_mods_list()
        ]
        assert id_list == [
            2290838143,
            463939057,
            1208939123,
            713709341,
            639837898,
            730310357,
            2011658088,
            2555651608,
            620260972,
            421908020,
            820924072,
            2260572637,
            450814997,
            497661914,
            541888371,
            497660133,
            333310405,
            825179978,
            861133494,
            1803586009,
            1858075458,
            1858070328,
            1808238502,
            1862208264,
            1841047025,
            939160383,
            1808723766,
            1598735666,
            2735613231,
            1779063631,
            2018593688,
        ]
