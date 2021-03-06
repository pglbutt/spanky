import os
import sys
import click

from spanky.config import Config


CONTEXT_SETTINGS = dict(auto_envvar_prefix='COMPLEX')


class Context(object):

    def __init__(self):
        self.verbose = False

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          'commands'))


class SpankyCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('spanky.commands.cmd_' + name,
                             None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=SpankyCLI, context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--verbose', is_flag=True,
              help='Enables verbose mode.')
@click.option('-c', '--config-dir', default='.',
              help='The path to the config files. DEFAULT: /etc/spanky')
@pass_context
def cli(ctx, verbose, config_dir):
    """Spanky the Devop."""
    ctx.verbose = verbose
    ctx.config = Config(config_dir)
