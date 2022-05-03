import logging

from sanic import Sanic
from srf.constant import ALL_METHOD
from srf.request import SRFRequest
from srf.routes import ViewSetRouter
from tortoise.contrib.sanic import register_tortoise

from views import TestView

logging.basicConfig(level=logging.DEBUG)
app = Sanic(__name__, request_class=SRFRequest)

route = ViewSetRouter()
route.register(TestView, '/TestView', 'test', True)
for i in route.urls:
    i.pop('is_base')
    app.add_route(**i, methods=ALL_METHOD)

register_tortoise(
    app, db_url="sqlite://:memory:", modules={"models": ['models']}, generate_schemas=True
)

# http://127.0.0.1:5000/TestView
if __name__ == "__main__":
    app.run(port=5000, auto_reload=True)
