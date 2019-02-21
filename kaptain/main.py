import click

from kaptain.report import report


@click.command()
def captain():
    """kaption egg"""
    print("Let's start coding...")
    pass


@click.group()
def cli():
    """Captain

    A modern deploy tool.
    """
    pass


cli.add_command(captain)
cli.add_command(report)

if __name__ == '__main__':
    captain()
    pass
