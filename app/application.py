import logging
import os
from config import Config
from flask_migrate import Migrate
from flask import Flask, request, current_app
from flask_appbuilder import AppBuilder, SQLA
from sqlalchemy import event
from sqlalchemy.engine import Engine
from app.index import MyIndexView
from logging.handlers import SMTPHandler, RotatingFileHandler



application = Flask(__name__)
app = application
app.config.from_object(Config)
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView, base_template='mybase.html')
migrate = Migrate(app, db)

if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/microblog.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Database startup')

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)



@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


from . import views, models  # noqa
