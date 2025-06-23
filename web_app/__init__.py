from flask import Flask
from mongoengine import connect
import configparser
import os
from dotenv import load_dotenv

def create_app():

    app = Flask(__name__)

    load_dotenv()

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config = configparser.ConfigParser()
    config.read(os.path.join(project_root, "config.ini"))

    Mongo_uri = None

    if os.getenv("DEPLOYMENT_MONGO_URI"):
        Mongo_uri = os.getenv("DEPLOYMENT_MONGO_URI")
        print("Connecting to MongoDB via DEPLOYMENT_MONGO_URI environment variable.")
    elif config.has_section("MongoDB") and config.has_option("MongoDB", "uri"):
        Mongo_uri = config.get("MongoDB", "uri")
        print("Connecting to Local MongoDB via config.ini")
    else:
        raise ValueError("Error in Connecting to MongoDB")

    app.config["MONGODB_SETTINGS"] = {
        "host": Mongo_uri,
        "db": "canucks_reddit_data",
        "alias": "default",
        "uuidRepresentation": "standard"

    }

    connect(**app.config["MONGODB_SETTINGS"])

    from .routes import bp
    app.register_blueprint(bp)

    return app

app = create_app()