from yhttp import json, validate, statuscode

from foo import app, __version__


@app.route(r'/')
@validate(nobody=True)
@json
@statuscode('200 Ok')
def describe(req):
    return dict(
        version=__version__
    )
