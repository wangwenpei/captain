"""
==================
执行抓取日志操作
==================
"""

import click


@click.group('fetch-log')
def fetch_log():
    """fetch log"""
    pass


@fetch_log.command()
def gcp():
    click.echo("hello world")
    pass
