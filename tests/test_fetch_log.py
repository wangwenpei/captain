import os


def test_fetch_log():
    """
    出于安全考虑，测试用例撰写时候，需要声明外部变量

    - KAPTAIN_FETCH_LOG_PROJECT

    example: kubernetes.var.log.containers.parity-nginx-mainnet
    -56cdc68c94-p6f28_nodefarm_parity-nginx
    -2219b8452634665a9e655da08cba1ff7225f3315de0581c9
    75d7df4a13c5fa03.log/2019/04/12
    :return:
    """

    from kaptain.main import fetch_log

    os.environ['KAPTAIN_FETCH_LOG_ROOT'] = os.path.join(
        os.path.dirname(__file__),
        "./test-resources")

    # os.environ['KAPTAIN_FETCH_LOG_BUCKET'] = 'archive-log'
    os.environ['KAPTAIN_FETCH_LOG_BUCKET'] = 'sre-demo-bucket'

    with fetch_log.make_context("[In-Dev]",
                                args=['gcp', 'raw_trans.json.log']) as ctx:
        result = fetch_log.invoke(ctx)
        pass

    # print(result.output)
    # print(result.exception)
    pass


def test_fetch_log_with_filter():
    from kaptain.main import fetch_log

    os.environ['KAPTAIN_FETCH_LOG_ROOT'] = os.path.join(
        os.path.dirname(__file__),
        "./test-resources")

    # os.environ['KAPTAIN_FETCH_LOG_BUCKET'] = 'archive-log'
    os.environ['KAPTAIN_FETCH_LOG_BUCKET'] = 'sre-demo-bucket'

    with fetch_log.make_context("[In-Dev]",
                                args=['gcp', 'raw_trans_with_filter.json.log',
                                      '--filter=log.json',
                                      ]) as ctx:
        result = fetch_log.invoke(ctx)
        pass

    print(result.output)
    print(result.exception)
    pass


def test_fetch_log_with_datefilter():
    from kaptain.main import fetch_log

    os.environ['KAPTAIN_FETCH_LOG_ROOT'] = os.path.join(
        os.path.dirname(__file__),
        "./test-resources")

    os.environ['KAPTAIN_FETCH_LOG_BUCKET'] = 'archive-log'
    # os.environ['KAPTAIN_FETCH_LOG_BUCKET'] = 'sre-demo-bucket'

    with fetch_log.make_context("[In-Dev]",
                                args=['gcp', 'raw_trans_with_date_filter.json.log',
                                      '--filter=tradebot-prod',
                                      '--date-filter=2019/05/30',
                                      '--display'
                                      ]) as ctx:
        result = fetch_log.invoke(ctx)
        pass

    print(result.output)
    print(result.exception)
    pass
