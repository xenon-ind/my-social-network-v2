import os
from pathlib import Path


def project_resource_dir():
    return Path(os.path.dirname(os.path.realpath(__file__))).parent.parent


def frontend_resource_dir():
    return project_resource_dir().joinpath(
        "src/client/frontend/deltanet-client-frontend/dist"
    )
