"""
    Author: lck
    Filename: config_parser.py
    Created: 19-09-2021
    Description:
"""

import json
import pathlib
from typing import Dict, Any, Tuple


class ConfigParser:
    """Read and manage .json configuration files."""

    def __init__(self, filename: str) -> None:
        """Initialize the class."""
        self.filename = filename
        self.config_dict: Dict[str, Any] = {}

        file_path, status = self._check_file_exists()
        if not status:
            raise FileNotFoundError(f"The Path: {file_path} does not exsist!")

    def _check_file_exists(self) -> Tuple[pathlib.Path, bool]:
        path = pathlib.Path().resolve() / self.filename
        return path, path.exists()

    def parse_config(self) -> None:
        """Generate dictionary of configuration key value pairs."""
        with open(self.filename, "r", encoding="utf-8") as file:
            self.config_dict = json.load(file)
