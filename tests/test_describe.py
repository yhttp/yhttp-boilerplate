from bddrest import status, response

from yhttp import boilerplate


def test_describe(app):

    with app('/', 'DESCRIBE'):
        assert status == 200
        assert response.json == dict(version=boilerplate.__version__)
