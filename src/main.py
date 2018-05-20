import curses
import locale
import logging
from time import sleep

from src.common.utils import colors as common_color_utils

logger = logging.getLogger(__name__)


def main(scr):

    # additional config
    curses.curs_set(0)
    curses.halfdelay(1)
    scr.clear()

    # set locale
    locale.setlocale(locale.LC_ALL, '')

    # vars
    key = 1

    # setup
    curses.start_color()
    curses.use_default_colors()
    common_color_utils.init()

    while key != ord('q'):  # quit on [q]
        try:
            # key handlers

            key = scr.getch()  # get the last key
            curses.flushinp()  # clear anything else the user has typed in
            scr.clear()

            # ...
            scr.addstr(1, 1, 'myapp')

            # refresh

            scr.noutrefresh()
            curses.doupdate()

        except Exception as e:
            logger.error("Unknown critical failure")
            print(e)
            sleep(2)
            break
