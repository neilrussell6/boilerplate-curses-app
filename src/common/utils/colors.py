import curses

from src.common.data.colors import color_pairs


def init():
    curses.start_color()
    curses.use_default_colors()
    [curses.init_pair(k, v[0], v[1]) for k, v in color_pairs.items()]
