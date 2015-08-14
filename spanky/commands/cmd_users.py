import click
from spanky.cli import pass_context
from spanky.lib.users import UserInit


@click.command('users', short_help='creates users base on /etc/spanky/users')
@pass_context
def cli(ctx):
    config = ctx.config.load('users.yml')()
    user_init = UserInit(config)
    user_init.build()
