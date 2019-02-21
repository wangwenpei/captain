"""
==========================
Report SRE operation
==========================
"""

import json
from configparser import ConfigParser
from datetime import datetime
from pathlib import Path

import click
import requests


def parse_config(git_config, use_private):
    c = ConfigParser()
    c.read(filenames=git_config)

    slack_channel = c.get('kaption', 'slack-channel', fallback=None)
    slack_private = c.get('kaption', 'slack-private', fallback=None)

    config = {
        "user": c.get('user', option='name', fallback=None),
        "email": c.get('user', option='email', fallback=None),
        "slack_channel": slack_private if use_private else slack_channel
    }
    return config


@click.command()
@click.option('--git-config',
              type=click.Path(exists=True),
              default="%s/.gitconfig" % Path.home(), envvar="GIT_CONFIG")
@click.option('--private',
              is_flag=True,
              default=False)
@click.argument('message')
def report(git_config, message, private):
    cli = click.get_current_context()
    config = parse_config(git_config, private)

    if config['slack_channel'] is None:
        cli.fail("no slack channel found,please set it.")
        pass

    ret = requests.post(
        config['slack_channel'],
        headers={
            'content-type': 'application/json'
        }, data=json.dumps({
            "text": '%(user)s operate %(message)s at %(datetime)s' % {
                'user': config['user'],
                'message': message,
                'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        }))

    ret.raise_for_status()
    # click.echo(ret.status_code)
    pass
