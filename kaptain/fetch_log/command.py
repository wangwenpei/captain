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
@click.option('--save-dir',
              type=click.Path(exists=True),
              default="/var/log/kaptain/gcp", envvar="KAPTAIN_FETCH_LOG_ROOT")
@click.option('--project',
              envvar="KAPTAIN_FETCH_LOG_PROJECT", required=True)
@click.option('--bucket-name',
              envvar="KAPTAIN_FETCH_LOG_BUCKET", required=True)
@click.argument('target')
@click.pass_context
def gcp(ctx, target, save_dir, project, bucket_name):
    """fetch gcp log

    """

    from google.cloud import storage

    storage_client = storage.Client(project)
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        blob.download_to_filename('%s/%s' % (save_dir, target))
        print(blob.name)

    pass
