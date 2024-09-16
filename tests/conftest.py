import functools

import pytest
import bddrest

from yhttp import boilerplate


@pytest.fixture
def app():
    boilerplate.app.ready()
    yield functools.partial(bddrest.Given, boilerplate.app)
    boilerplate.app.shutdown()
