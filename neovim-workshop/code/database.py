"""
    Author: lck
    Filename: database.py
    Created: 05-09-2021
    Description:
"""
# import mariadb #sudo apt-get install libmariadb3 libmariadb-dev
from typing import Dict, Tuple, TypedDict, Optional, Any, Iterator
from dataclasses import asdict
from transform import Worker
import pymysql
from termcolor import colored


class DBConnectionError(Exception):
    """Custom error type if pymysql cant connect to database."""


class Credential(TypedDict):
    """Database connection dict."""

    database: str
    host: str
    port: int
    user: str
    password: str


class DBConnectionHandler:
    """Context Manager for database connetion."""

    def __init__(self, connection_dict: Credential) -> None:
        """INIT."""
        self.connection_dict = connection_dict
        self.connection: Optional[pymysql.Connection] = None  # type: ignore

    def __enter__(self) -> pymysql.Connection:  # type: ignore
        """Connect to the database."""
        self.connection = pymysql.connect(**self.connection_dict)
        return self.connection

    def __exit__(
        self, exc_type: Any, exc_value: Any, exc_traceback: Any
    ) -> None:
        """Close the database connection."""
        if self.connection is not None:
            self.connection.close()


def collect_data_from_db(
    login_credentials: Credential, counter: int
) -> Iterator[Tuple[Any, ...]]:
    """Connect to the database and read out the table Mitarbeiter."""
    try:
        with DBConnectionHandler(login_credentials) as conn:
            statement = """SELECT * FROM Mitarbeiter;"""
            cur = conn.cursor()
            cur.execute(statement)

            data_list = (cur.fetchone() for _ in range(counter))
            return data_list

    except pymysql.err.OperationalError as e:
        message = colored(
            (
                f"Can't connect to MySQL server on '"
                f"{login_credentials.get('host')}:"
                f"{login_credentials.get('port')}'\n"
                f"Please check if your docker container is running!"
            ),
            "red",
        )
        raise DBConnectionError(message) from e

def transform_db_data(data_set: Tuple[Any, ...]) -> Dict[str, Any]:
    """Transform database data to Worker objects and json."""
    worker_object = Worker(*data_set)
    worker_object.get_censored_password()
    return asdict(worker_object)
