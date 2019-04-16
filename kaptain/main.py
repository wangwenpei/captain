import click

from kaptain import captain
from kaptain.fetch_log.command import fetch_log
from kaptain.report import report


@click.group()
@click.option('--debug', default=False,
              envvar='KAPTAIN_DEBUG')
@click.pass_context
def cli(ctx, debug):
    """Kaptain

    A modern SRE tool.
    """
    ctx.obj = captain.Captain(debug)
    pass


cli.add_command(report)
cli.add_command(fetch_log)

if __name__ == '__main__':
    cli(obj={})
    pass
