import logging
from abc import ABC, abstractmethod
from typing import List

from interactive_steamcmd_wrapper import ISteamCMDProcess, InteractiveSteamCMD

from steam_server_manager.common.steam_credentials import STEAM_CREDENTIALS, get_token
from steam_server_manager.common.workshopmod import WorkshopMod


class SteamGameServer(ABC):
    def __init__(
        self,
        steam_installer: InteractiveSteamCMD,
        app_install_dir: str,
        mods_install_dir: str,
    ):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.steam = steam_installer
        self.app_install_dir = app_install_dir
        self.mods_install_dir = mods_install_dir

    @property
    @abstractmethod
    def app_id(self) -> int:
        ...

    @property
    @abstractmethod
    def game_id(self) -> int:
        ...

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

    @abstractmethod
    def prepare_bash_file(self, mods: List[WorkshopMod]) -> None:
        ...
