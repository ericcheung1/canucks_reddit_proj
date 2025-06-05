from flask import Flask
from mongoengine import connect
import configparser
import os

def create_app():

    app = Flask(__name__)

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config = configparser.ConfigParser()
    config.read(os.path.join(project_root, "config.ini"))

    mongo_host = config.get("MongoDB", "server")
    mongo_db_name = config.get("MongoDB", "database")

    connect(db=mongo_db_name, host=mongo_host)

    from .routes import bp

    app.register_blueprint(bp)

    return app
