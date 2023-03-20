"""
    Author: lck
    Filename: app.py
    Created: 05-09-2021
    Description: main file
"""
from web import start_flask_server
from database import Credential
from config_parser import ConfigParser


def main() -> None:
    """ENTRY POINT."""
    # parse config.json file
    parser = ConfigParser("config.json")
    parser.parse_config()

    # get data from database
    database_credentials: Credential = {
        "database": parser.config_dict.get('databaseName'), #type: ignore
        "host": parser.config_dict.get('hostName'), #type: ignore
        "port": parser.config_dict.get('port'), #type: ignore
        "user": parser.config_dict.get('username'), #type: ignore
        "password": parser.config_dict.get('password') #type: ignore
    }

    # start the web server
    start_flask_server(database_credentials)


if __name__ == "__main__":
    main()
