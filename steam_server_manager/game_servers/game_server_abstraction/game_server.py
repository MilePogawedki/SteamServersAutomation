from abc import ABC, abstractmethod
from typing import List


class SteamGameServer(ABC):
    @property
    @abstractmethod
    def app_id(self) -> int:
        ...

    @property
    @abstractmethod
    def app_install_dir(self) -> str:
        ...
        ...

    @property
    @abstractmethod
    def mods_install_dir(self) -> str:
        ...

    @property
    @abstractmethod
    def game_id(self) -> str:
        ...

    @abstractmethod
    def update_app(self) -> None:
        ...

    @abstractmethod
    def update_workshop_mods(self, mods_id: List[int]) -> None:
        ...

    @abstractmethod
    def prepare_bash_file(self) -> None:
        ...
