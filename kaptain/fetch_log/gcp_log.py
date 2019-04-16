"""
======================
下载GCP日志到本地存储
======================
"""

import click


@click.command()
@click.option('--save-dir',
              type=click.Path(exists=True),
              default="/var/log/kaptain/gcp", envvar="KAPTAIN_FETCH_LOG_ROOT")
@click.option('--project',
              envvar="KAPTAIN_FETCH_LOG_PROJECT", required=True)
@click.option('--bucket',
              envvar="KAPTAIN_FETCH_LOG_BUCKET", required=True)
@click.pass_context
def gcp(save_dir, project, bucket):
    """fetch gcp log"""

    click.echo("hello")
    pass
