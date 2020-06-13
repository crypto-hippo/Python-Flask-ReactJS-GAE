from flask import Blueprint, request, jsonify

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth.route("/test")
def test(*args, **kwargs):
    return "API is functional"


