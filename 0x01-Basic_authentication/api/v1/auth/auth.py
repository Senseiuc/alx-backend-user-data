#!/usr/bin/env python3
"""
Auth Class: Task 3
"""
from typing import List, TypeVar

from flask import request


class Auth:
    """
    a class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if the required auth is given
        :param path:
        :param excluded_paths:
        :return:
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Checks for authorisation header
        :param request:
        :return:
        """

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user
        :param request:
        :return:
        """
        return None
