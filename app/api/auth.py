import re

from flask import (
    Blueprint,
    Response,
    request,
    abort
)
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from app.data_models.user import UserData
from app.utils.datas import POST
from app.utils.funcs import dict_as_data


__all__ = ["route"]

route = Blueprint("auth", __name__)


@route.post("/register")
def post_register():
    args: POST = request.parse(['username', 'email', 'password'])

    if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', args.email):
        return abort(400)

    try:
        user = User(dict_as_data(args, UserData()))
        user.add(user)
        return Response(status=200)
    except IntegrityError:
        return abort(400)


@route.post("/login")
def post_login():
    args: POST = request.parse(['password'])

    if args.username:
        user = User.query.filter(User.username == args.username).first()
    elif args.email:
        user = User.query.filter(User.email == args.email).first()
    else:
        return abort(400)

    if user and user.verify_password(args.password):
        return Response(status=200)

    return abort(401)


@route.post("/logout")
def post_logout():
    # TODO logout_user
    return Response(status=200)
