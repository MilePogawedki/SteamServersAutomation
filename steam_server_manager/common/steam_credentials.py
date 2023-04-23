import os

from steam_totp import generate_twofactor_code_for_time

if not os.environ["STEAM_USERPASS"]:
    raise Exception("No credentials in env variables STEAM_USERPASS (ex. 'user,pass')")

STEAM_CREDENTIALS = tuple(os.environ["STEAM_USERPASS"].split(":"))
SECRET = os.environ["FA_SECRET"]


def get_token():
    return generate_twofactor_code_for_time(SECRET)
