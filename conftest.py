import pytest
from Library.app import LIBRARY_SERVER


@pytest.fixture(scope='module')
def client():
    yield LIBRARY_SERVER.app.test_client()

