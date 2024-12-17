from flask import Flask, jsonify

from  .extensions import *
from .config import Config


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    # app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png"]
    # app.config["UPLOAD_PATH"] = "image_uploads"
    if test_config is not None:
        app.config.update(test_config)

    # api.init_app(app)
    # jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    return app

"""
# jwt error handlers
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify({"message": "Token has expired", "error": "token_expired"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
            {"message": "Signature verification failed", "error": "invalid_token"}
        ),
        401,
    )

@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify(
            {
                "message": "Request doesnt contain valid token",
                "error": "authorization_header",
            }
        ),
        401,
    )

@jwt.token_in_blocklist_loader
def token_in_blocklist_callback(jwt_header, jwt_data):
    jti = jwt_data['jti']
    db = get_db()
    query = db.execute("select get_jti_or_none(%s)", (jti,)).fetchone()
    if query is None:
        token = None
    else:
        token = query['get_jti_or_none']

    # token = db.session.query(TokenBlocklist).filter(TokenBlocklist.jti == jti).scalar()

    return token is not None

# load user
@jwt.user_lookup_loader
def user_lookup_callback(jwt_header, jwt_data):
    id = int(jwt_data['sub'])
    db = get_db()
    user = db.execute("select get_user_by_id(%s);", (id,)).fetchone()['get_user_by_id']
    return user if user else None

@jwt.additional_claims_loader
def make_additionnal_claim(identity):
    id = int(identity)
    db = get_db()
    user_role = db.execute("select get_user_by_id(%s);", (id,)).fetchone()['get_user_by_id'][2]
    context = {'user_role': user_role}
    return context
"""