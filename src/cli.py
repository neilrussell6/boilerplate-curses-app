import curses
import logging

import click
import click_log
from src.main import main

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.group()
@click.version_option(version='0.1.0')
def cli():
    pass


@cli.command()
def run():
    curses.wrapper(main)
