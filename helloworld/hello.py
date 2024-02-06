from pathlib import Path
import os
import sys
import connexion

from connexion.resolver import RelativeResolver




if getattr(sys, "frozen", False):  # detect if the program has been compiled with pyinstaller
    SPEC_FOLDER = os.path.join(sys._MEIPASS, "spec")
else:
    SPEC_FOLDER = "spec"

app = connexion.FlaskApp(__name__, specification_dir=SPEC_FOLDER)
app.add_api(
    "swagger.yaml",
    arguments={"title": "Hello World Example"},
    resolver=RelativeResolver("helloworld"),
)


def post_greeting(name: str) -> str:
    return f"Hello {name}"
