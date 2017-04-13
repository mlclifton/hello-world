import pytest


def test_function():
    pass


@pytest.fixture()
def a_fixture():
    pass


def test_that_uses_a_fixture(a_fixture):
    pass
