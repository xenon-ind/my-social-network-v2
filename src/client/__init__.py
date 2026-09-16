import threading
import time

import webview
from flask import Flask, send_from_directory
from loguru import logger

from client.utils import frontend_resource_dir, project_resource_dir
from client.webviewapi import WebViewAPI

app = Flask(__name__, static_folder=frontend_resource_dir() / "app")


@app.route("/")
def index():
    return send_from_directory(frontend_resource_dir(), "index.html")


@app.route("/<path:path>")
def serve(path):
    return send_from_directory(frontend_resource_dir(), path)


def main():
    logger.debug("Hello, world!")

    logger.debug(f"Project resource dir: '{project_resource_dir()}'.")
    logger.debug(f"Frontend resource dir: '{frontend_resource_dir()}'.")

    threading.Thread(target=lambda: app.run(port=5000), daemon=True).start()
    time.sleep(1)

    webview.create_window(
        "DeltaNet client",
        url="http://localhost:5000",
        js_api=WebViewAPI(),
        min_size=(400, 300),
    )
    webview.start(debug=True)


if __name__ == "__main__":
    main()
