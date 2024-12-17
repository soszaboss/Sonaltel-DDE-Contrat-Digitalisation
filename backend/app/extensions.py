from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from flask_admin import Admin

from flask_migrate import Migrate

# from flask_jwt_extended import JWTManager

# from flask_smorest import Api


# Setup Flask-Admin
admin = Admin(name='admin', template_mode='bootstrap5')

# Setup Flask-SQL-ALchemy
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# Setup Flask-Migrate
migrate = Migrate()

# Setup Flask-JWT
# jwt = JWTManager()

# Flask-Smorest
# api = Api(spec_kwargs={})