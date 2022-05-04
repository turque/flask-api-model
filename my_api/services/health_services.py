from flask import current_app
from flask.json import dumps

ready = True


def liveness():
    status = 200
    message = "UP"
    return _make_response(status, message)


def readiness():
    status = 200
    message, ready = service_status()
    if not ready:
        status = 503
    return _make_response(status, message)


def _make_response(status, message):
    return current_app.response_class(
        dumps(message),
        status=status,
        content_type="application/problem+json",
    )


def service_status():
    # if any dependency is out the service is not ready to receive request
    services = {
        "DB": db_probe(),
    }
    if "DOWN" in services.values():
        return services, False
    else:
        return services, True


def db_probe():
    # TODO implement db conecion test
    return "UP"
