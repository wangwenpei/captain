import pytest
from click.testing import CliRunner

pytest_plugins = []  # pre-defined


def pytest_namespace():
    return {
        'cli_runner': CliRunner(),  # global runner
    }


@pytest.fixture(scope='function')
def cli_runner():
    """custom cli runner,
    if you really need it.
    """
    return CliRunner()
