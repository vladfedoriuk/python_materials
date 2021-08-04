import os


dirname = os.path.dirname(__file__)


class DebugConfig(object):
    DEBUG = True
    SECRET_KEY = "something-secret"
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        os.path.abspath(dirname), "course.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
