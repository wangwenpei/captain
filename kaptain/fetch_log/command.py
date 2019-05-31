"""
==================
执行抓取日志操作
==================
"""

import click


# from ..captain import Captain
# pass_captain = click.make_pass_decorator(Captain)


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
@click.option('--filter', default='')
@click.option('--date-filter', default='')
@click.option('--display/--no-display', default=False)  # 临时策略
@click.argument('target')
# @pass_captain
@click.pass_context
def gcp(ctx, target, save_dir, project, bucket_name, filter, date_filter,
        display):
    """fetch gcp log"""

    from google.cloud import storage

    storage_client = storage.Client(project)
    bucket = storage_client.get_bucket(bucket_name)
    write_file = '%s/%s' % (save_dir, target)

    blobs = bucket.list_blobs()

    with open(write_file, 'ab') as fp:
        for blob in blobs:
            if filter in blob.name:
                if date_filter is '' or date_filter in blob.name:
                    if display:
                        print('将会下载的日志文件:', blob.name)
                    else:
                        string_buffer = blob.download_as_string()
                        fp.write(string_buffer)
            # else:
            #     # todo:: 集成Logger
            #     print(blob.name, '跳过匹配')

    pass
