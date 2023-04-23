import os.path

from interactive_steamcmd_wrapper import InteractiveSteamCMD

from steam_server_manager.game_servers.arma_3_server.arma_3_html_mod_parser import Arma3HtmlModParser
from steam_server_manager.game_servers.arma_3_server.arma_3_server import Arma3Server


def run_arma_3_server_updater(isteam: InteractiveSteamCMD):
    server = Arma3Server(isteam)
    server.update_app()


def run_arma_3_mods_updater(isteam: InteractiveSteamCMD):
    server = Arma3Server(isteam)
    with open(os.path.join(os.getcwd(), "a3mods.html"), "r") as file:
        raw_html = file.read()
    mod_list = Arma3HtmlModParser(raw_html).get_mods_list()
    server.update_workshop_mods(mod_list)
