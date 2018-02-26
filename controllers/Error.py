import json
from tornado.web import RequestHandler
from library.Result import Result


class NotFoundHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(404)
        self.write(json.dumps(Result(code=404, msg="NOT FOUND!").json()))
