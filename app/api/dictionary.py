from flask import Blueprint, request

from app.models.word import Word
from app.data_models.word import WordData
from app.api.base import BaseResource
from app.utils.datas import (
    GET,
    POST,
    DELETE,
    PATCH
)

__all__ = ["route"]

route = Blueprint("dictionary", __name__, url_prefix="dictionary")


@route.get("/")
def get():
    args: GET = request.parse()

    return BaseResource.get(Word, args)


@route.post("/")
def post():
    args: POST = request.parse(["word"])

    return BaseResource.post(Word, args)


@route.delete("/")
def delete():
    args: DELETE = request.parse(["id"])

    return BaseResource.delete(Word, args)


@route.patch("/")
def patch():
    args: PATCH = request.parse(["id", "attr", "value"])

    return BaseResource.patch(Word, WordData, args)
