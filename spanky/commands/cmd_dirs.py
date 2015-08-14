import sys

import click

from spanky.cli import pass_context
from spanky.lib.dirs import DirInit


@click.command('dirs', short_help='creates dirs base')
@pass_context
def cli(ctx):
    try:
        config = ctx.config.load('dirs.yml')
    except IOError:
        # no config lets bail
        click.echo('No dirs to install')
        sys.exit(1)

    user_init = DirInit(config)
    user_init.build()
