from flask import Flask, send_from_directory

from client.utils import frontend_resource_dir

flask_app = Flask(__name__, static_folder=frontend_resource_dir() / "app")


@flask_app.route("/")
def index():
    return send_from_directory(frontend_resource_dir(), "index.html")


@flask_app.route("/<path:path>")
def serve(path):
    return send_from_directory(frontend_resource_dir(), path)
