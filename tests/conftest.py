import pytest
from epics_linter.linter import Linter


@pytest.fixture(scope="session")
def linter():
    linter = Linter()
    yield linter
