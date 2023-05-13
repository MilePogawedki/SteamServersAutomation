import logging

import click
from interactive_steamcmd_wrapper import InteractiveSteamCMD, ISteamCMDAlreadyInstalled

from steam_server_manager.game_servers.arma_3_server.main import run_arma_3_server_updater, run_create_bash_file
from steam_server_manager.game_servers.arma_3_server.main import run_arma_3_mods_updater


def get_isteam() -> InteractiveSteamCMD:
    return InteractiveSteamCMD("/home/steam/steamcmd")


@click.group()
def cmd():
    logging.basicConfig(level=logging.DEBUG)


@cmd.command()
def install_steam():
    try:
        get_isteam().install()
    except ISteamCMDAlreadyInstalled:
        pass


@cmd.command()
def install_arma_3_server():
    run_arma_3_server_updater(get_isteam())


@cmd.command()
def install_arma_3_mods():
    run_arma_3_mods_updater(get_isteam())


@cmd.command()
def prepare_bash_file():
    run_create_bash_file(get_isteam())
