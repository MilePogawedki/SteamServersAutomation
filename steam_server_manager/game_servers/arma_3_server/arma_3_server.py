from typing import List

from interactive_steamcmd_wrapper import InteractiveSteamCMD

from steam_server_manager.common.workshopmod import WorkshopMod
from steam_server_manager.game_servers.game_server_abstraction.game_server import SteamGameServer


class Arma3Server(SteamGameServer):
    @property
    def app_id(self) -> int:
        return 233780

    @property
    def game_id(self) -> int:
        return 107410

    def __init__(
        self,
        steam_installer: InteractiveSteamCMD,
        app_install_dir: str = "/home/steam/steamapps/arma_3_server",
        mods_install_dir: str = "/home/steam/",
    ):
        super().__init__(steam_installer, app_install_dir, mods_install_dir)

    def prepare_bash_file(self, mods: List[WorkshopMod]) -> None:
        raise NotImplementedError
