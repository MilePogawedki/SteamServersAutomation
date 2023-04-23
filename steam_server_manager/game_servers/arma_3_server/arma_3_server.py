import logging
from typing import List

from interactive_steamcmd_wrapper import ISteamCMDProcess, InteractiveSteamCMD

from steam_server_manager.common.steam_credentials import STEAM_CREDENTIALS, get_token
from steam_server_manager.common.workshopmod import WorkshopMod
from steam_server_manager.game_servers.game_server_abstraction.game_server import SteamGameServer


class Arma3Server(SteamGameServer):
    game_id = 107410
    app_id = 233780
    app_install_dir = "/home/steam/steamapps/arma_3_server"
    mods_install_dir = "/home/steam/"

    def __init__(self, steam_installer: InteractiveSteamCMD):
        self.logger = logging.getLogger(__class__.__name__)
        self.steam = steam_installer

    def update_app(self) -> None:
        steam_cmd: ISteamCMDProcess
        with self.steam.run() as steam_cmd:
            steam_cmd.login(*STEAM_CREDENTIALS, get_token())
            steam_cmd.update_app(
                self.app_id,
                self.app_install_dir,
            )

    def update_workshop_mods(self, mods: List[WorkshopMod]) -> None:
        steam_cmd: ISteamCMDProcess
        with self.steam.run() as steam_cmd:
            steam_cmd.login(*STEAM_CREDENTIALS, get_token())
            for mod in mods:
                self.logger.info("Installing <%s>", mod.mod_name)
                steam_cmd.update_workshop_mod(
                    self.game_id,
                    mod.mod_id,
                    "/home/steam/",
                )

    def prepare_bash_file(self) -> None:
        raise NotImplementedError
