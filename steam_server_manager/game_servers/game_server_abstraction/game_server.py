import logging
import os
from abc import ABC, abstractmethod
from typing import List, Dict

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

    def update_workshop_mods(self, mods: Dict[int, WorkshopMod]) -> None:
        mods_location: str = "/home/steam/"
        steam_cmd: ISteamCMDProcess
        with self.steam.run() as steam_cmd:
            steam_cmd.login(*STEAM_CREDENTIALS, get_token())
            for mod in mods.values():
                self.logger.info("Installing <%s>", mod.mod_name)
                steam_cmd.update_workshop_mod(
                    self.game_id,
                    mod.mod_id,
                    mods_location,
                )
        self._rename_files_to_lowercase(os.path.join(mods_location, "steamapps/workshop"))
        self._symlink_all_mods(mods)

    @staticmethod
    def _rename_files_to_lowercase(location: str) -> None:
        os.system("find " + location + " -depth -exec rename 's/(.*)\\/([^\\/]*)/$1\\/\\L$2/' {} \\;")

    def _symlink_all_mods(self, mods: Dict[int, WorkshopMod]) -> None:
        local_mods_path = os.path.join(self.app_install_dir, "mods")
        if not (os.path.exists(local_mods_path) and os.path.isdir(local_mods_path)):
            os.mkdir(os.path.join(local_mods_path))

        location = "/home/steam/steamapps/workshop/content/107410/"
        for filename in os.listdir(location):
            source = os.path.join(location, filename)
            target = os.path.join(local_mods_path, mods[int(filename)].simplified_mod_name)
            self.logger.info("Adding a symlink between from <%s> to <%s>", source, target)
            os.symlink(source, target)

    @abstractmethod
    def prepare_bash_file(self, mods: List[WorkshopMod]) -> None:
        ...
