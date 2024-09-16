from yhttp.core import json, statuscode, text

from .rollup import app


@app.route(r'/')
@app.bodyguard(strict=True)
@text
@statuscode('200 Ok')
def get(req):
    return "Welcome to yhttp\n"


@app.route(r'/')
@app.bodyguard(strict=True)
@json
@statuscode('200 Ok')
def describe(req):
    return dict(
        version=app.version
    )
