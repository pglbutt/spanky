import click
from spanky.cli import pass_context


@click.command('echo', short_help='echos something, or nothing')
@click.argument('words', required=False)
@pass_context
def cli(ctx, words):
    """Echos a thing"""
    if words is None:
        words = 'You said nothin\''
    if ctx.verbose:
        words += " VERBOSELY"
    click.echo(words)
    ctx.log('Logging something to stderr')
