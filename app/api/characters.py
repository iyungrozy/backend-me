from flask import Blueprint, request

from app.api.base import BaseResource
from app.data_models.character import CharacterData
from app.models.character import Character
from app.utils.datas import (
    GET,
    POST,
    DELETE,
    PATCH
)

__all__ = ["route"]

route = Blueprint("characters", __name__, url_prefix="characters")


@route.get("/")
def get():
    args: GET = request.parse()

    return BaseResource.get(Character, args)


@route.post("/")
def post():
    args: POST = request.parse(["name", "name_en"])

    return BaseResource.post(Character, args)


@route.delete("/")
def delete():
    args: DELETE = request.parse(["id"])

    return BaseResource.delete(Character, args)


@route.patch("/")
def patch():
    args: PATCH = request.parse(["id", "attr", "value"])

    return BaseResource.patch(Character, CharacterData, args)
