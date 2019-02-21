import pytest


def test_main():
    from kaptain.main import captain

    result = pytest.cli_runner.invoke(captain)
    assert "Let's start coding..." == result.output.strip()
    pass
