import random
from magicstats import *
from MagicRecord import *
from Magicplaycond import *


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!magic':
        return tonight()

    if p_message == '!record':
        return "Orlando Magic is Currently at " + wins + " wins and " + loss + " losses"

    if p_message == '!standing':
        return "Orlando Magic Standing: " + standing + "th Out of 15 in the Eastern Conference"

    if message == 'roll':
        return str(random.randint(1,6))

    if p_message == '!help':
        return '`Commands to run Magic Bot:' \
               '\n!magic - Checks if Magic are playing today' \
               '\n!standing - Current standing in the Eastern Conference' \
               '\n!record - Magic Record`'

#    return 'I didn\'t undertstand what you said. Try typing "!help".'