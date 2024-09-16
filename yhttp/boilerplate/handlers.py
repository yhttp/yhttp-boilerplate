from yhttp.core import json, statuscode

from .rollup import app


@app.route(r'/')
@app.bodyguard(strict=True)
@json
@statuscode('200 Ok')
def describe(req):
    return dict(
        version=app.version
    )
