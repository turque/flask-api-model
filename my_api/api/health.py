from flask import Blueprint
from flask_restful import Api, Resource

from my_api.services.health_services import liveness, readiness


class Liveness(Resource):
    def get(self):
        return liveness()


class Readiness(Resource):
    def get(self):
        return readiness()


blueprint = Blueprint("health", __name__, url_prefix="/")
api = Api(blueprint)
api.add_resource(Liveness, "health/live")
api.add_resource(Readiness, "health/ready")
