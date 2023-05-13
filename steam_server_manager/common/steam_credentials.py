import os
import logging

from steam_totp import generate_twofactor_code_for_time

if "STEAM_USERPASS" not in os.environ.keys():
    logging.getLogger("steam_credentials").warning("No credentials in env variables STEAM_USERPASS (ex. 'user,pass')")

STEAM_CREDENTIALS = tuple(os.environ["STEAM_USERPASS"].split(":"))
SECRET = os.environ["FA_SECRET"]


def get_token():
    return generate_twofactor_code_for_time(SECRET)
