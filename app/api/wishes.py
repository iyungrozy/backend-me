from flask import (
    Blueprint,
    Response,
    request,
    abort
)
from sqlalchemy.exc import IntegrityError

from app.api.base import BaseResource
from app.data_models.wish import WishData
from app.models.wish import Wish
from app.utils.datas import (
    GET,
    POST,
    DELETE,
    PATCH
)

__all__ = ["route"]

route = Blueprint("wishes", __name__, url_prefix="wishes")


@route.get("/")
def get():
    args: GET = request.parse()

    if args.id is not None:
        wishes = Wish.find_entity(Wish, args.id)
    elif args.start is not None and args.end is not None:
        wishes = Wish.find_entities(Wish, args.start, args.end)
    elif args.start is not None:
        wishes = Wish.find_entities_starting_with(Wish, args.start)
    elif args.end is not None:
        wishes = Wish.find_entities_starting_with(Wish, args.end)
    else:
        wishes = Wish.get_all_entities(Wish)

    if wishes is None:
        return abort(404)

    if isinstance(wishes, list) and len(wishes) != 0:
        return [item.as_dict(args.ignore) for item in wishes]
    elif isinstance(wishes, list) and len(wishes) == 0:
        return abort(404)
    elif wishes:
        return wishes.as_dict(args.ignore)
    else:
        return abort(404)

    # for wish in wishes:
    #     wish_dict: dict = wish.as_dict()
    #     rate_4_dict = {
    #         "rate_4": [{rate_4.character_id: Character.find_entity(Character, rate_4.character_id).name} for rate_4
    #                    in Wish.db.session.query(rate_four_association).filter(rate_four_association.c.wishes_id == wish.id).all()]}
    #
    #     if row := Wish.db.session.query(rate_five_association).filter(rate_five_association.c.wishes_id == wish.id).first():
    #         rate5_dict = {"rate_5": {row.character_id: Character.find_entity(Character, row.character_id).name}}
    #     else:
    #         rate5_dict = {"rate_5": {}}
    #
    #     wish_dict.update(rate_4_dict)
    #     wish_dict.update(rate5_dict)
    #     list_wishes.append(wish_dict)


@route.post("/")
def post():
    args: POST = request.parse(["title", "title_en"])

    entity = Wish(args)
    # todo create relationship
    # if not rate5:
    #     if character5 := Character.query.filter(Character.id == rate5).first():
    #         entity.rate_5 = character5
    #     else:
    #         return status404
    # if not rate4:
    #     for rate in rate4:
    #         if character4 := Character.query.filter(Character.id == rate).first():
    #             entity.rate_4.append(character4)
    #         else:
    #             return status404

    try:
        Wish.update(entity)
    except IntegrityError:
        return abort(400)
    return Response(status=200)


@route.delete("/")
def delete():
    args: DELETE = request.parse(["id"])

    return BaseResource.delete(Wish, args)



@route.patch("/")
def patch():
    args: PATCH = request.parse(["id", "attr", "value"])

    return BaseResource.patch(Wish, WishData, args)
