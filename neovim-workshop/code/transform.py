"""
    Author: lck
    Filename: transform.py
    Created: 05-09-2021
    Description:
"""
from dataclasses import dataclass


@dataclass
class Worker:
    """Datamodel for table Mitarbeiter."""

    identifier: int
    first_name: str
    last_name: str
    age: int
    email: str
    gender: str
    username: str
    password: str
    image_path: str

    def get_censored_password(self) -> None:
        """Only show first two characters of password."""
        censored_password: str = ""
        i: int
        char: str
        for i, char in enumerate(self.password):
            censored_password += char if i < 2 else "*"
        self.password = censored_password
