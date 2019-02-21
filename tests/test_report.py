import pytest


def test_report():
    from kaptain.main import report

    with report.make_context("[In-Dev]", args=['aaa']) as ctx:
        result = report.invoke(ctx)
        pass

    result = pytest.cli_runner.invoke(report, args=[
        'hello world',
        '--private'
    ])
    print(result.output)
    print(result.exception)
    pass
