from flask import Blueprint, request

from app.models.weapon import Weapon
from app.data_models.weapon import WeaponData
from app.api.base import BaseResource
from app.utils.datas import (
    GET,
    POST,
    DELETE,
    PATCH
)

__all__ = ["route"]

route = Blueprint("weapons", __name__, url_prefix="weapons")


@route.get("/")
def get():
    args: GET = request.parse()

    return BaseResource.get(Weapon, args)


@route.post("/")
def post():
    args: POST = request.parse(["title", "title_en"])

    return BaseResource.post(Weapon, args)


@route.delete("/")
def delete():
    args: DELETE = request.parse(["id"])

    return BaseResource.delete(Weapon, args)


@route.patch("/")
def patch():
    args: PATCH = request.parse(["id", "attr", "value"])

    return BaseResource.patch(Weapon, WeaponData, args)
