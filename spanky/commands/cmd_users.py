import sys

import click

from spanky.cli import pass_context
from spanky.lib.users import UserInit


@click.command('users', short_help='creates users base on /etc/spanky/users')
@pass_context
def cli(ctx):
    try:
        config = ctx.config.load('users.yml')()
    except IOError:
        # no config lets bail
        click.echo('No users to install')
        sys.exit(1)

    user_init = UserInit(config)
    user_init.build()
