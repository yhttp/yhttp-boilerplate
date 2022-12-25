from bddrest import status, response


def test_info_info(app):
    import foo

    with app('/', 'DESCRIBE'):
        assert status == 200
        assert response.json == dict(version=foo.__version__)
