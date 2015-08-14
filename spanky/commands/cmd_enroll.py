import sys
import subprocess

import click

from spanky.cli import pass_context
from spanky.lib.enroll import enroll


@click.command('enroll', short_help='Enroll / leave',
               context_settings=dict(ignore_unknown_options=True))
@click.option('--name', '-n')
@click.option('--host', '-H')
@click.option('--port', '-p')
@click.argument('cmd', nargs=-1, type=click.UNPROCESSED)
@pass_context
def cli(ctx, name, host, port, cmd):
    config = ctx.config.load('enroll.yml')
    with enroll(config, name, host, port):
        sys.exit(subprocess.call(' '.join(cmd), shell=True))
