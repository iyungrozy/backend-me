from flask import (
    Blueprint,
    Response,
    request,
    abort
)

from app.api.base import BaseResource
from app.models.meta import Meta
from app.utils.datas import (
    GET,
    POST,
    DELETE,
    PATCH
)

__all__ = ["route"]

route = Blueprint("meta", __name__, url_prefix="meta")


@route.get("/")
def get():
    args: GET = request.parse()

    if (result := Meta.get_by_attr(Meta, args.attr)) is None:
        return abort(404)

    return result.as_dict(args.ignore)


@route.post("/")
def post():
    args: POST = request.parse(["attr", "value"])

    return BaseResource.post(Meta, args)


@route.delete("/")
def delete():
    args: DELETE = request.parse(["attr"])

    if entity := Meta.get_by_attr(Meta, args.attr):
        Meta.delete(entity)
        return Response(status=200)
    else:
        return abort(404)


@route.patch("/")
def patch():
    args: PATCH = request.parse(["attr", "value"])

    if entity := Meta.get_by_attr(Meta, args.attr):
        entity.__setattr__("value", args.value)
        entity.update(entity)
        return Response(status=200)
    else:
        return abort(404)
