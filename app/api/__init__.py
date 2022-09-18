from flask import Blueprint

from app.api import (
    auth,
    characters,
    dictionary,
    meta,
    weapons,
    wishes
)


api: Blueprint = Blueprint('api', __name__)

api.register_blueprint(auth.route)
api.register_blueprint(characters.route)
api.register_blueprint(dictionary.route)
api.register_blueprint(meta.route)
api.register_blueprint(weapons.route)
api.register_blueprint(wishes.route)
