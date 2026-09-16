import threading
import time

import webview
from loguru import logger

from client.flask import app
from client.utils import frontend_resource_dir, project_resource_dir


def main():
    logger.debug("Hello, world!")

    logger.debug(f"Project resource dir: '{project_resource_dir()}'.")
    logger.debug(f"Frontend resource dir: '{frontend_resource_dir()}'.")

    threading.Thread(target=lambda: app.run(port=5000), daemon=True).start()
    time.sleep(1)

    webview.create_window(
        "DeltaNet client",
        url="http://localhost:5000",
        min_size=(400, 300),
    )
    webview.start(debug=True)


if __name__ == "__main__":
    main()
