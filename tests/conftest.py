import functools

import pytest
import bddrest

import foo


@pytest.fixture
def app():
    foo.app.ready()
    yield functools.partial(bddrest.Given, foo.app)
    foo.app.shutdown()
