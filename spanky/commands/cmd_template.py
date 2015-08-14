import os
import json

import click
from jinja2 import Environment

from spanky.cli import pass_context


@click.command('template', short_help='writes a template')
@click.argument('template')
@click.argument('values', type=click.File('rb'))
@pass_context
def cli(ctx, template, values):
    cfg_dir = ctx.config.base

    template_file = os.path.join(cfg_dir, template)
    f = _open_file(template_file, 'r')
    jtemplate = Environment().from_string(f.read())

    values = json.load(values)

    rendered = jtemplate.render(**values)

    click.echo(rendered)


def _open_file(filename, mode):
    try:
        return open(filename, mode)
    except IOError:
        click.echo("Couldn't find %s" % filename)
        raise click.Abort()
