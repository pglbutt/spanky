import click
from spanky.cli import pass_context


@click.command('users', short_help='creates users base on /etc/spanky/users')
@pass_context
def cli(ctx):
    config = ctx.config
