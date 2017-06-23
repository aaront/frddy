# -*- coding: utf-8 -*-

"""
frddy.cli
~~~~~~~~~
Contains the code to handle the CLI
"""

import click

from . import core

@click.command()
@click.argument('urlpath')
def url(urlpath: str):
    '''Reports info about the JSON endpoint to the console window'''
    res = core.analyze_url(urlpath)
    click.echo(res.type.name)

@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def local(filepath: str):
    """Reports info about a local JSON file to the console window"""
    res = core.analyze_file(filepath)
    click.echo(res.type.name)

@click.group()
@click.version_option()
def main():
    """frddy"""
    pass

main.add_command(url)
main.add_command(local)
