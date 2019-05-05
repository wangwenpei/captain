import click

from kaptain import captain
from kaptain.fetch_log.command import fetch_log
from kaptain.report import report
# from kaptain.ws import ws


@click.group()
@click.option('--debug', default=False,
              envvar='KAPTAIN_DEBUG')
@click.option('--dry-run', default=False)
@click.option('-v', '--verbose', count=True)
@click.pass_context
def cli(ctx, debug, dry_run, verbose):
    """Kaptain

    A modern SRE tool.
    """
    ctx.obj = captain.Captain(debug, dry_run, verbose)
    pass


cli.add_command(report)
cli.add_command(fetch_log)
# cli.add_command(ws)

if __name__ == '__main__':
    cli(obj={})
    pass
