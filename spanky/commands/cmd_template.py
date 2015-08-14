import os
import json

import click
from jinja2 import Environment

from spanky.cli import pass_context


@click.command('template', short_help='writes a template')
@click.argument('template')
@click.argument('value_path')
@click.argument('destination')
@pass_context
def cli(ctx, template, value_path, destination):
    cfg_dir = ctx.config.base

    template_file = os.path.join(cfg_dir, template)
    f = _open_file(template_file, 'r')
    jtemplate = Environment().from_string(f.read())

    value_path = os.path.join(cfg_dir, value_path)

    try:
        values = json.load(_open_file(value_path, 'r'))
    except ValueError:
        click.echo("Invalid json in %s" % value_path)
        raise click.Abort()

    rendered = jtemplate.render(**values)

    with open(destination, 'w+') as f:
        f.write(rendered)


def _open_file(filename, mode):
    try:
        return open(filename, mode)
    except IOError:
        click.echo("Couldn't find %s" % filename)
        raise click.Abort()
