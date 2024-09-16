from yhttp.core import Application


app = Application()


# Add builtin settings here
app.settings.merge('''
auth:
  redis:
    host: localhost
    port: 6379
    db: 0

  token:
    algorithm: HS256
    secret: foobar

  refresh:
    key: yhttp-refresh-token
    algorithm: HS256
    secret: quxquux
    secure: true
    httponly: true
    maxage: 2592000  # 1 Month
    domain: example.com
''')


@app.when
def ready(app):
    from . import __version__
    app.version = __version__


# http handlers
from . import handlers
