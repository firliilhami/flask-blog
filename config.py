import os

basedir = os.path.dirname(__file__)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 2525)
    MAIL_USE_TLS = True # os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '9689877281d769'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '71e2047fc941ff'
    ADMINS = ['firli.pad@gmail.com']
    TESTING = False
    MAIL_SUPPRESS_SEND = False

    POSTS_PER_PAGE = 3
