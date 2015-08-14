import json

import click

from spanky.cli import pass_context
from spanky.lib.enroll import roster


@click.command('roster', short_help='Enroll / leave')
@click.argument('name')
@pass_context
def cli(ctx, name):
    config = ctx.config.load('enroll.yml')
    click.echo(json.dumps(list(roster(config, name))))
