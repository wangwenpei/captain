import os


def test_fetch_log():
    from kaptain.main import fetch_log

    os.environ['KAPTAIN_FETCH_LOG_ROOT'] = os.path.join(
        os.path.dirname(__file__),
        "./test-resources")

    os.environ['KAPTAIN_FETCH_LOG_BUCKET'] = 'archive-log'
    os.environ['KAPTAIN_FETCH_LOG_BUCKET'] = 'sre-demo-bucket'

    with fetch_log.make_context("[In-Dev]",
                                args=['gcp', 'raw_trans.log.json']) as ctx:
        result = fetch_log.invoke(ctx)
        pass

    print(result.output)
    print(result.exception)
    pass
