from bddrest import status, response


def test_describe(app):

    with app('/', 'GET'):
        assert status == 200
        assert response.text == "Welcome to yhttp\n"
