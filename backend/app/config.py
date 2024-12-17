import datetime
import os
import dotenv

dotenv.load_dotenv()

class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # FLASK_ADMIN_SWATCH="darkly"

    # lorsqu'une exception est levée dans une extension,
    # elle est transmise à l'application Flask principale afin que vous puissiez la voir plus facilement.
    PROPAGATE_EXCEPTIONS = os.getenv('PROPAGATE_EXCEPTIONS')

    """
    # Configuration du JWT
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=60)
    """

    """
    # Configuration d'Open API et de la documentaion
    API_TITLE = os.getenv('API_TITLE')
    OPENAPI_VERSION = os.getenv('OPENAPI_VERSION')
    API_VERSION = os.getenv('API_VERSION')
    OPENAPI_JSON_PATH = os.getenv('OPENAPI_JSON_PATH')
    OPENAPI_URL_PREFIX = os.getenv('OPENAPI_URL_PREFIX')
    OPENAPI_REDOC_PATH = os.getenv('OPENAPI_REDOC_PATH')
    OPENAPI_REDOC_URL = os.getenv('OPENAPI_REDOC_URL')
    OPENAPI_SWAGGER_UI_PATH = os.getenv('OPENAPI_SWAGGER_UI_PATH')
    OPENAPI_SWAGGER_UI_URL = os.getenv('OPENAPI_SWAGGER_UI_URL')
    OPENAPI_RAPIDOC_PATH = os.getenv('OPENAPI_RAPIDOC_PATH')
    OPENAPI_RAPIDOC_URL = os.getenv('OPENAPI_RAPIDOC_URL')
    """


