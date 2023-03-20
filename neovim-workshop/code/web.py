"""
    Author: lck
    Filename: web.py
    Created: 05-09-2021
    Description: flask webserver to display the database data
"""
import json
from typing import Optional, Dict, Any, cast
from flask import Flask
from database import Credential, collect_data_from_db, transform_db_data, DBConnectionError

app = Flask(__name__)


@app.route("/")
def main_page() -> str:
    """Render the startpage."""
    return "Hello World!"


@app.route("/getUser/<int:number>")
def return_user(number: int) -> str:
    """Return n users from the database formatted as json."""
    db_credentials: Optional[Credential] = app.config.get("db_credentials")
    output_dict: Dict[str, Any] = {"Data": []}

    if not db_credentials:
        raise TypeError("Error")

    if number > cast(int, app.config.get("MAX_RETURN")):
        return "Error 404"

    try:
        database_data = collect_data_from_db(db_credentials, number)

    except DBConnectionError as e:
        print("Logging: ", e)
        return "DB Error"

    output_dict["Data"] = [transform_db_data(data) for data in database_data]
    return json.dumps(output_dict)


def start_flask_server(database_credentials: Credential) -> None:
    """Start Flask server in a different thread."""
    app.config["db_credentials"] = database_credentials
    app.config["MAX_RETURN"] = 1_000
    app.run(port=4444, debug=True)
